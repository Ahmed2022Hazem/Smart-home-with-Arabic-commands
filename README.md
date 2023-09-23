# Smart-home-with-Arabic-commands
Introduction : 

The concept of smart homes has gained significant attention in recent years due to the rapid advancement of technology and the growing need for energy-efficient and sustainable living.
Smart homes use advanced technology to automate and control various household functions, such as lighting, heating, ventilation, air conditioning, security, and entertainment.
However, most existing smart home control systems primarily focus on English-based voice commands, limiting accessibility for non-English speakers and neglecting the specific needs of diverse linguistic communities.
This project aims to bridge this gap by developing a smart home control system that operates through audio commands  in the Arabic language.

Abstract :

The aim of this project is to develop a smart home control system that operates through audio commands spoken in the Arabic language. The system integrates Google API for accurate speech recognition and natural language processing. 
The primary focus was on enabling the system to differentiate between different users’ voices by utilizing voice recognition technology, providing personalized access and control over various smart home devices.
The system stays in sleep mode until a chosen wakeup word is said then it waits for commands to control the appliances.

Project’s components : 

1.	Speech recognition:

Speech recognition is used for Identifying the commands to be applied on the appliances by changing the spoken words to text by using Goggle API then the generated text is tested to see if it is the same as one of the commands .
2.	Voice recognition:

Voice recognition is used to differentiate between different speakers so that each has a personalized experience and prevent unauthorized persons from controlling the devices.
Each user has hundreds of 1 second audio files which are used to train a neural network and this training is saved in a model which is used to process new audio data to detect the user.

3.	Users database:

Each user must sign up first and enter his username, email, and password.
Each username is then connected with the audio data of the speaker to be able to login with his voice.
The login process is done automatically by saying the wakeup word.

4.	Controlling devices:

The devices are controlled using the Arduino.
A Bluetooth module is mounted on the Arduino where it receives the commands from the laptop then these commands are interpreted to actions through the code written in the Arduino.
The commands were specified to control a led lamp and a model of a curtain which operates by 2 DC motors whose rotation is controlled by H bridge module.

5.	User interface:
The user interface is completely written in Arabic to be the same as the language of speaking.
The user interface is divided into two widgets, one for the account of the user who signed in and the other for controlling the appliances. 

Result : 
The LED lamp and the curtains followed the instructions as planned for them.
The system succeeded in registering new users and saving their data in a database.
Staying in sleep mode until the wakeup word is said was successful. 
Signing in with the audio of the wakeup word was successful.
Differentiating between different users was successful with reasonable accuracy.
However, the system didn’t achieve its goal in allowing only authorized people to control the appliances.
