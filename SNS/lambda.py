import sys
sys.path.insert(0, '/opt')

import boto3
import slackweb

sns = boto3.client('sns')

def lambda_handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    slack = slackweb.Slack(url='https://hooks.slack.com/services/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')
    slack.notify(text=str(message),channel="#exercicio-sns-serverless", username="doctorpoint-team", icon_emoji=":squirrel: :shitpit:")