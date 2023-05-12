TurtleBot Mozgatás

A TurtleBotunkat a Gazeboo emulátorba helyezzük.

A feladat, hogy az elé kerülő akadályokat észlelje, és megpróbálja kikerülni.
Ehhez a LIDAR szenzort fogjuk használni. Feliratkozunk a LIDAR Scan topicjára és publisholunk velocity parancsokat a cmd_vel topicnak, hogy az akadályok közt navigáljunk.

Így, ha a robot meglát egy akadályt, megpróbál elfordulni, hogy tudja folytatni az útját. 
