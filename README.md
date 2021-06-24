# Airtel Telecommunications Smart REST API SDK

Provides a set of classes to build subscription, transactions funnel, payment gateway
and operator discovery enterprise APIs

_Export environment variables_

    $ export SERVER_IP = <server_ip>
    $ export SERVER_PORT = <server_port>

This package seeks to help Python developers implement the various Airtel Money APIs without much Challenges

string json =   "{\"InitiatorName\":\" here\"," +
                 "\"SecurityCredential\":\" here \"," +
                 "\"CommandID\":\" here \"," +
                 "\"Amount\":\" here \"," +
                 "\"PartyA\":\" here \"," +
                 "\"PartyB\":\" here \"," +
                 "\"Remarks\":\" here \"," +
                 "\"QueueTimeOutURL\":\"http://your_timeout_url\"," +
                 "\"ResultURL\":\"http://your_result_url\"," +
                 "\"Occasion\":\" here \"}";

Write the json string to a Stream which will be sent along with your request.

using (var streamWriter = new StreamWriter(request.GetRequestStream()))
{
//the string (json) should be here
streamWriter.Write(json);
streamWriter.Flush();
streamWriter.Close();
}

How to use ?

Insert data to the API request body as stated above example.
Insert the actual token to "ACCESS_TOKEN";
Use your application consumer key for this field "YOUR_APP_CONSUMER_KEY"
Use your application consumer secret for this field "YOUR_APP_CONSUMER_SECRET".
Development

Python ^ Pycharm 2021 & .NET Framework 4.6.4 & 
Visual Studio Code 2020 are required. JayDwayne™