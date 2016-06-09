import boto3

# Setup AWSAccountsService client
client = boto3.client(service_name='AWSAccountsService')
# Email address for the new AWS account
newAccountEmail='vadlakha@yahoo.com'
# Remember that the service's account needs permission to post to this topic
notificationSNSArn='arn:aws:sns:us-east-1:066894140628:AWSOrganizationsTopic'
# Set the name of the IAM role the payer will use to access the account
IAMRoleName='PayerAccountAccessRole'
newAccountAddress={
            "firstName": "John",
            "lastName": "Smith",
            "mailingAddress": {
              "addressLine1": "1918 8th Ave",
              "addressLine2": "thisLineOptional",
              "addressLine3": "thisLineOptional",
              "city": "Seattle",
              "stateOrRegion": "Washington",
              "postalCode": "98101-1210",
              "countryCode": "US"
            },
            "phoneNumber": "1234567890"
          }

res=client.create_linked_account(email=newAccountEmail, address=newAccountAddress, snsArn=notificationSNSArn, roleName=IAMRoleName)
print(res)