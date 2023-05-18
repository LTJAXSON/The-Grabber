# The-Grabber

**A Simple Honeypot that log ssh connection's & username's & password's**

--------------------------------------------------------------

## Using scenario:

**Let's say you have an organization that has a ssh server and you expect only authorized employees to authenticate to the server. you may change the ssh orignal server port to something that only the emplloyees know about it, then using the-grabber, you can put it as port 21 which is the default ssh port and log any activite on it. once you have notice some connection's (as the employess wont authenticate on honeypot server) you may use a snort rule to reject any connection's from that ip address and see if any account is actually compromise and the password is known. **
