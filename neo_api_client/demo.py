# from neo_api_client import NeoAPI
import io
import neo_api_client
import threading


def on_message(message):
    print('[Res]: ', message)


def on_error(message):
    result = message
    print('[OnError]: ', result)

login_session = {'consumer_key': 'WOfozyccBiHXuGdrCtTktf6MNiMa', 'consumer_secret': 'dnvkSMsppsBt50LMytUmY4BD4Jwa', 'host': 'prod', 'base64_token': 'V09mb3p5Y2NCaUhYdUdkckN0VGt0ZjZNTmlNYTpkbnZrU01zcHBzQnQ1MExNeXRVbVk0QkQ0Sndh', 'bearer_token': 'eyJ4NXQiOiJNbUprWWpVMlpETmpNelpqTURBM05UZ3pObUUxTm1NNU1qTXpNR1kyWm1OaFpHUTFNakE1TmciLCJraWQiOiJaalJqTUdRek9URmhPV1EwTm1WallXWTNZemRtWkdOa1pUUmpaVEUxTlRnMFkyWTBZVEUyTlRCaVlURTRNak5tWkRVeE5qZ3pPVGM0TWpGbFkyWXpOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjbGllbnQ5MTY4IiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiJXT2ZvenljY0JpSFh1R2RyQ3RUa3RmNk1OaU1hIiwibmJmIjoxNzIwNzU3MTAzLCJhenAiOiJXT2ZvenljY0JpSFh1R2RyQ3RUa3RmNk1OaU1hIiwic2NvcGUiOiJkZWZhdWx0IiwiaXNzIjoiaHR0cHM6XC9cL25hcGkua290YWtzZWN1cml0aWVzLmNvbTo0NDNcL29hdXRoMlwvdG9rZW4iLCJleHAiOjE3MjA4NDM1MDMsImlhdCI6MTcyMDc1NzEwMywianRpIjoiODdmZTllNDktNzk2Yi00OWFkLTg3NjYtMTZhZjg2YThjOGUwIn0.INgNVW7gvaUcy8cF6PoQ4QO5GmSb-GQT2mIYXyy614CNz_uuaVLtuBuDVtRbSx0Pi3I-WieF8B4NPscNzRRRiMNldx-TZWJWJJmAfV6r4NZdsoqlfanRoCjKUaFAk-rjGUUkUA6Q5zCHxXZjPOH9Xnyd1w3A7Vkh7YmnMVoKzJmWv-2OIFSn89RNSM7s3TNj3-B8r99bLSAlRGL48E8yleNZFtJEfeR-byp-bwFqDZt1uhNVp1OknQU8UbKZa646r01p8rHOrN6Df2lfbieQeIUnyOSLITs8F33tuSZeahq2dmlECP9qCcuKb06pBmyn8edizVuKJfh4B0JRxc3bfA', 'view_token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJWaWV3Il0sImV4cCI6MTcyMDgwOTAwMCwianRpIjoiNDRhZDU1OTQtNGQ3Ni00ZGE1LTk3NDgtMzJjZTA5NDM1OGIzIiwiaWF0IjoxNzIwNzU3MTE4LCJpc3MiOiJsb2dpbi1zZXJ2aWNlIiwic3ViIjoiOWE3Zjg4YzktZjJjMS00NGVhLTkxZTEtNTdkYTlhMDg4NjVhIiwidWNjIjoiWFZJSzYiLCJuYXAiOiIiLCJ5Y2UiOiJlWVxcNlwiIyQ1PXdcdTAwMDVcblx1MDAwNWdcdTAwMDBcdTAwMTBiIiwiZmV0Y2hjYWNoaW5ncnVsZSI6MCwiY2F0ZWdvcmlzYXRpb24iOiIifQ.QbcPqYNDbhoP2wy2DCrj_Y1pgnVfB0jnl6EItzl4wb1CyxvMX_tzu89lXhCVKoTuaWPjPKmKiscQJ_7jQhBbG2b-ek5P7JSU3OcG3bX2Z8XsrRyUQ0kuYWfrmGDVxR0hmuTvOGkEVW3fhWiZnw0Q551jTEBgq_YeTxFv9luCIWNDDP1dqB1CrDHlY7quta7Nmu7vzKmd-qscLTVKaDW0vscgbx2Xus_jmZhrbABpJQPkaor2-JiGFZLuI_LhGOI6VUXCgLovgfCrkdFGaVJMxv5O6DmDoziNLx-PSYB0iT1OdkYEvRORFn-9KFOG3wqZWekMXor7lLqv7r4gyyEgmw', 'sid': '99d040e3-37ce-4b1a-ae09-235088d1c146', 'userId': '9a7f88c9-f2c1-44ea-91e1-57da9a08865a', 'edit_token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJUcmFkZSJdLCJleHAiOjE3MjA4MDkwMDAsImp0aSI6IjU0OGIzYTQ3LTU2YTgtNDQ4NC1iMzQ0LWE5MzBiMDI1ZDUwNCIsImlhdCI6MTcyMDc1NzE0NywiaXNzIjoibG9naW4tc2VydmljZSIsInN1YiI6IjlhN2Y4OGM5LWYyYzEtNDRlYS05MWUxLTU3ZGE5YTA4ODY1YSIsInVjYyI6IlhWSUs2IiwibmFwIjoiIiwieWNlIjoiZVlcXDZcIiMkNT13XHUwMDA1XG5cdTAwMDVnXHUwMDAwXHUwMDEwYiIsImZldGNoY2FjaGluZ3J1bGUiOjAsImNhdGVnb3Jpc2F0aW9uIjoiIn0.bDX8S3mm0mQXfzlXqDI6O4yGXFJ2N7MShZ9vY9ghXTBuFOgw2DN66ToqG9m3MskTLVRREv_guPSWQcro0uXI1epAVWPmF-R0nCQbL5Elz8e50Pt65ysZGQqN8KAFQfTEgxQILpV8VVlf_cgTNireV9pBO2PpGhNc0r_KBLQxy7MUIvoYqJ-T6JK9jlpabteMoFFkOHeKgwvQU4LTlxoATUaVhLRRkLFmuUzTAY-58KSCQXQAlrSnXOU7YV-ILlwxQNamiwLBwmjXj9HeCkN1ykBIp5_f4GZFZ0bNgvtYpjob63c4J-by_XNXfHOGzf55g3gxW0kdwatEpsF-zma7GA', 'edit_sid': '99d040e3-37ce-4b1a-ae09-235088d1c146', 'edit_rid': '9ef210d9-a332-414a-83ef-6ea5366a7a46', 'serverId': 'server1', 'login_params': {'pan': 'CHJPR7530Q', 'password': 'Secured@#$89'}, 'neo_fin_key': None}

# client = neo_api_client.NeoAPI(consumer_key="WOfozyccBiHXuGdrCtTktf6MNiMa",
#                                consumer_secret="dnvkSMsppsBt50LMytUmY4BD4Jwa", environment='prod')
# client = neo_api_client.NeoAPI(access_token='',
#                                environment='prod', on_message=on_message,
#                                on_error=on_error)
client = neo_api_client.NeoAPI(
    login_session=login_session
)
# client.login(pan="CHJPR7530Q", password="Secured@#$89")
# otp = input("otp : ")
# a = client.session_2fa(otp)
# print(a)
# access_token = a['data']['token']
# print(client.search_scrip(exchange_segment="nse_fo", symbol="ICICI", expiry="", option_type="CE",strike_price=">505"))
print(client.search_scrip(exchange_segment="nse_fo", symbol="BANKNIFTY", expiry="", option_type="CE",strike_price="45000"))
# client.subscribe_to_orderfeed()
# print(type(a))
print('---------------------------------------------------')
print(client.configuration)