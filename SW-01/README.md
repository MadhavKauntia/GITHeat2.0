# SW-01
This is a Python script to get information about a Codeforces user or about upcoming contests using the Codeforces API. The libraries required to run this script are argparse, requests and datetime.

## Instructions to run

* To find details like name, rating, rank, location or profile picture of a particular user.
`python app.py --handle <user-handle>`
OR
`python app.py -H <user-handle>`

* To find details of upcoming contests.
`python app.py --contests`
OR
`python app.py -c`