This is all about creating a Flask web server and Deploying in Heroku

Created a Application in Heroku. Connect to github Repository from Heroku.

                                        https://flaskpal.herokuapp.com
                                        

HOST YOUR CODE IN github from Git Version Control software

Create different API's for        

                                  1) Basic checks, 
                                    https://flaskpal.herokuapp.com/
                                    
                                  2) API call Method - GET - /hello-world
                                    https://flaskpal.herokuapp.com/hello-world
                                    
                                  3) API call Method - POST -/check-palindrome/{VALUES} --> can check from POSTMAN tool.
                                    https://flaskpal.herokuapp.com/check-palindrome
                                  
                                  4) API call Method - GET -/check-count --> count of Page visit of /Check-palindrome
                                    https://flaskpal.herokuapp.com/check-count

Error handled for incorrect url.

Using POSTMAN to check the above api call-
                                Method - GET- https://flaskpal.herokuapp.com/hello-world
                                Method - POST https://flaskpal.herokuapp.com/check-palindrome
                                               POST BODY - jason format 
                                               {
	                                                "value":["Time","a","malam"]
                                                }
