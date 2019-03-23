from slackclient import SlackClient

slack_token = os.environ["xoxp-304305798082-304290752420-586003127986-139dfcdb18eb3fb007ac2817c72b68bd"]
sc = SlackClient(slack_token)

# sc.api_call(
#     "chat.postMessage",
#     channel="shithole",
#     text="Hello from Python! :tada:"
# )