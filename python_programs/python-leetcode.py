import leetcode
leetcode_session = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNjQ3NjI2NSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6Ijc3ZjViYjFkM2U1YTg2ZDQwMTdjYzE2NmM1ZWQxNDRjZTNmYzZmZjIiLCJpZCI6NjQ3NjI2NSwiZW1haWwiOiJ0b255c3RhcmthdmVuZ2VyMThAZ21haWwuY29tIiwidXNlcm5hbWUiOiJ0b255c3RhcmthdmVuZ2VyMTgiLCJ1c2VyX3NsdWciOiJ0b255c3RhcmthdmVuZ2VyMTgiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvYXZhdGFycy9hdmF0YXJfMTY1MzYyMDQxMS5wbmciLCJyZWZyZXNoZWRfYXQiOjE2NTYxMjEzODgsImlwIjoiMjQwMjo4MTAwOjI4NDI6ODE4ZDplODVmOmUwNzA6YzQ5NTo2MDM0IiwiaWRlbnRpdHkiOiJkODhhMDNmMTE3NTg0NmM5YTYxMGRiOTI3MWYxYjExYiIsInNlc3Npb25faWQiOjIyODk3OTE0fQ.DVIcJ0wfipWeSXnjPrLGZCFfvLFP0HSWFCkLPt-t2Kw'

csrf_token = '2XiUTz38Ez3ZfOgAWvQcLoBJQx8XksSlxw94ZpsI9hX4lBaJj1lklCKnKva6Hou0'

configuration = leetcode.Configuration()
configuration.api_key["x-csrftoken"] = csrf_token
configuration.api_key["csrftoken"] = csrf_token
configuration.api_key["LEETCODE_SESSION"] = leetcode_session
configuration.api_key["Referer"] = "https://leetcode.com"
configuration.debug = False
api_instance =leetcode.DefaultApi(leetcode.ApiClient(configuration))
graphql_request = leetcode.GraphqlQuery(
query="""
     {
       user {
            username
            isCurrentUserPremium
         }
     }
     """,
variables=leetcode.GraphqlQueryVariables(),
)
print(api_instance.graphql_post(body=graphql_request))
api_response=api_instance.api_problems_topic_get(topic="algorithms")
solved_questions=[]
for questions in api_response.stat_status_pairs:
    if questions.status=="ac":
       solved_questions.append(questions.stat.question__title)
print(solved_questions)
print("Total number of solved questions ",len(solved_questions))
