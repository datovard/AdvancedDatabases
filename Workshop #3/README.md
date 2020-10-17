# Workshop #3

In this workshop we are going to address HBase as my first approach to NoSQL database schemas

## Challenge Description

The social network Twitter can be understood as a community of users who follow and are followed by others
users. The tracking relationship is not symmetrical, i.e. if a user A follows a user B , it does not imply
that user B follows user A. As part of its system, Twitter Inc. allows the user to follow or stop
follow users, see the list of users that follow, see the list of users that follow.

Lately Twitter is hiring expert staff to improve its database system and as part of
of the interview process has given you the task of designing a data model in Hbase that allows you to
efficient way to perform the following access patterns:

* Reads: 
    * List users followed by the user ```X```
    * Determine if a user ```X``` follows user ```Y```
    * List the users that follow user ```X```
* Writes:
    * User ```X``` follows a new user ```Y```
    * User ```X``` stops following a user ```Y```

## Previous steps

### How to run an HBase Docker instance?

This project have a docker-compose file where you can find the image used, the volumes used to persist data and the mapping of the ports. Run this command on your console or terminal, be sure that your terminal is on 

```
docker-compose up -d
```

To check if your instance is up and running HBase, enter this URL on your browser:

```
http://localhost:16010/master-status
```

You must see a status report of the HBase process running

### How to access your instance and run HBase terminal commands?

First, you must access your docker instance. To do this, run this command:

```
docker exec -it <your instance name or ID> /bin/bash
```

If you cloned or downloaded this repo, our command with instance name must be something like:

```
docker exec -it workshop3_database_1 /bin/bash
```

If you want to run it on another folder, copy the docker-compose.yml of this workshop and paste it on your project. To get the name of your instance, run this command:

```
docker ps -a
```

The name of your instance should appear on the image name of *dajobe/hbase* and must look something like this (check the name at the end of this result):

```
CONTAINER ID        IMAGE                          COMMAND                  CREATED             STATUS                  PORTS                                                                                                                                                                                                                    NAMES
bbba6090f9f2        dajobe/hbase                   "/opt/hbase-server"      17 minutes ago      Up 17 minutes           0.0.0.0:2181->2181/tcp, 0.0.0.0:2888->2888/tcp, 8080/tcp, 8085/tcp, 9090/tcp, 0.0.0.0:3888->3888/tcp, 0.0.0.0:16000->16000/tcp, 0.0.0.0:16010->16010/tcp, 0.0.0.0:16020->16020/tcp, 0.0.0.0:16030->16030/tcp, 9095/tcp   workshop3_database_1
```

Once you entered the instance, run this command to send *queries* to your HBase instance:

```
hbase shell
```

Now you can access your own HBase instance in Docker really easy!

