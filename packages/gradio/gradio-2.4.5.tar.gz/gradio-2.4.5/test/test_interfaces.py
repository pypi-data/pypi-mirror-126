import tempfile
from gradio.interface import *
import unittest
import unittest.mock as mock
import requests
import sys
from contextlib import contextmanager
import io
import threading

os.environ["GRADIO_ANALYTICS_ENABLED"] = "False"

@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class TestInterface(unittest.TestCase):
    
    # send_error_analytics should probably actually be a method of Interface
    # (so it doesn't have to take the 'enabled' argument)
    # and since it's specific to the launch method, it should probably be
    # renamed to send_launch_error_analytics.
    # these tests test its current behavior
    @mock.patch("requests.post")
    def test_error_analytics_doesnt_crash_on_connection_error(self, mock_post):
        mock_post.side_effect = requests.ConnectionError()
        send_error_analytics(True)
        mock_post.assert_called()
        
    @mock.patch("requests.post")
    def test_error_analytics_doesnt_post_if_not_enabled(self, mock_post):
        send_error_analytics(False)
        mock_post.assert_not_called()
     
    @mock.patch("requests.post")   
    def test_error_analytics_successful(self, mock_post):
        send_error_analytics(True)
        mock_post.assert_called()
                
    # as above, send_launch_analytics should probably be a method of Interface
    @mock.patch("requests.post")
    def test_launch_analytics_doesnt_crash_on_connection_error(self, mock_post):
        mock_post.side_effect = requests.ConnectionError()
        send_launch_analytics(analytics_enabled=True,
                              inbrowser=True, is_colab="is_colab",
	                              share="share", share_url="share_url")
        mock_post.assert_called()
        
    @mock.patch("requests.post")
    def test_launch_analytics_doesnt_post_if_not_enabled(self, mock_post):
        send_launch_analytics(analytics_enabled=False,
                              inbrowser=True, is_colab="is_colab",
	                              share="share", share_url="share_url")
        mock_post.assert_not_called()
     
    def test_reset_all(self):
        interface = Interface(lambda input: None, "textbox", "label")
        interface.close = mock.MagicMock()
        reset_all()
        interface.close.assert_called()
        
    def test_examples_invalid_input(self):
        with self.assertRaises(ValueError):
            Interface(lambda x: x, examples=1234)
        
    def test_examples_not_valid_path(self):
        with self.assertRaises(FileNotFoundError):
            interface = Interface(lambda x: x, "textbox", "label", examples='invalid-path')
            interface.launch()
            interface.close()
            
    def test_test_launch(self):
        with captured_output() as (out, err):
            prediction_fn = lambda x: x
            prediction_fn.__name__ = "prediction_fn"
            interface = Interface(prediction_fn, "textbox", "label")
            interface.test_launch()
            output = out.getvalue().strip()
            self.assertEqual(output, 'Test launch: prediction_fn()... PASSED')
            
    @mock.patch("time.sleep")
    def test_run_until_interupted(self, mock_sleep):
        with self.assertRaises(KeyboardInterrupt):
            with captured_output() as (out, err):
                mock_sleep.side_effect = KeyboardInterrupt()
                interface = Interface(lambda x: x, "textbox", "label")
                interface.enable_queue = False
                thread = threading.Thread()
                thread.keep_running = mock.MagicMock()
                interface.run_until_interrupted(thread, None)
                output = out.getvalue().strip()
                self.assertEqual(output, 'Keyboard interruption in main thread... closing server.')


    @mock.patch('gradio.utils.colab_check')
    def test_launch_colab_share(self, mock_colab_check):
        mock_colab_check.return_value = True
        interface = Interface(lambda x: x, "textbox", "label")
        _, _, share_url = interface.launch(prevent_thread_lock=True)
        self.assertIsNotNone(share_url)
        interface.close()
    
    
    @mock.patch('gradio.utils.colab_check')
    @mock.patch('gradio.networking.setup_tunnel')
    def test_launch_colab_share_error(self, mock_setup_tunnel, mock_colab_check):
        mock_setup_tunnel.side_effect = RuntimeError()
        mock_colab_check.return_value = True
        interface = Interface(lambda x: x, "textbox", "label")
        _, _, share_url = interface.launch(prevent_thread_lock=True)
        self.assertIsNone(share_url)
        interface.close()
    
    def test_interface_representation(self):
        prediction_fn = lambda x: x
        prediction_fn.__name__ = "prediction_fn"
        repr = str(Interface(prediction_fn, "textbox", "label")).split('\n')
        self.assertTrue(prediction_fn.__name__ in repr[0])
        self.assertEqual(len(repr[0]), len(repr[1]))
        
    def test_interface_load(self):
        io = Interface.load("models/distilbert-base-uncased-finetuned-sst-2-english", alias="sentiment_classifier")
        output = io("I am happy, I love you.")
        self.assertGreater(output['Positive'], 0.5)
        
    def test_interface_none_interp(self):
        interface = Interface(lambda x: x, "textbox", "label", interpretation=[None])
        scores, alternative_outputs = interface.interpret(["quickest brown fox"])
        self.assertIsNone(scores[0])
    
    @mock.patch('webbrowser.open')
    def test_interface_browser(self, mock_browser):
        interface = Interface(lambda x: x, "textbox", "label")
        interface.launch(inbrowser=True, prevent_thread_lock=True)
        mock_browser.assert_called_once()
        interface.close()
            
    def test_examples_list(self):
        examples = ['test1', 'test2']
        interface = Interface(lambda x: x, "textbox", "label", examples=examples)
        interface.launch(prevent_thread_lock=True)
        self.assertEqual(len(interface.examples), 2)
        self.assertEqual(len(interface.examples[0]), 1)
        interface.close()

    # def test_launch_counter(self):
    #     with tempfile.TemporaryFile(suffix=".json", mode="r+") as tmp:
    #         with mock.patch('gradio.interface.JSON_PATH', tmp.name):
    #             launches = {"launches": 1}
    #             json.dump(launches, tmp)
    #             print(">>>>", tmp.name, json.load(tmp.name))
    #             interface = Interface(lambda x: x, "textbox", "label")
    #             interface.launch(prevent_thread_lock=True)
    #             interface.launch(prevent_thread_lock=True)
            
    # example attribute of Interface can be a list or string. When it is a string, it is a filepath.
    # The content of this filepath will determine the examples. Do we have any sample of this example file?
    # This will help writing a test for lines 297 to 313 of interface.py. We need the log.csv example file 

if __name__ == '__main__':
    unittest.main()