# Introduction #

We are ready with our final product for PayPal's month long Raspeberry Pi hackathon. It was a tough job designing this product but when we look at it now, we know it was worth it. So we are going to see this project step by step and by the end, you will be able to make this project straight from scratch. Good luck 😉 

### The Problem: Cabs at PayPal ###

PayPal is a great place to work. It loves its employees (**PyPl**) so much that it provides them with a free cab drop and pick up services from their homes to the office and back. But here is a small problem that comes up. The Taxi contractors need to maintain a daily log of the number of people using the cab and therefore the driver passes a thick register to every person sitting inside the Taxi to fill their details every time.
Now here comes the problem:

* The passangers need to make the entry in the moving cab and it becomes a clumpsy affair.
* We are living in 2018, why waster paper?



### The Solution: *<u>Coco</u>* ###

To tackle the above problem we developed **Coco**, A completely customizable and Open Source Taxi companion. Now let's see how Coco will be solving the above problems along with taking your Cab riding experience to a next level.Let's have a look that her functionalities:

* She is completely **voice controlled**. That means you don't need a display to interact with her and you can use her while driving. Also she is going to guide you at every step by verbose responses.
* She can recognize a person entering in the cab (realtime) with the help of a camera module with an accuracy of ***99.38%***.
* She has a RFID reader that can read the passanger's card to make their attendence.
* She can log your GPS location accurately and can tell you the excat address and time from where you boarded the cab and vice - versa.
* She has a great sense of humour ( say "**Joke**")
* She can help you lookup for any english word meaning (say " *word*")
* She will read out the latest news headlines for you ( say "**News**")



### Modules used: ###

* [PiCamera module](https://www.amazon.in/Raspberry-5MP-Camera-Board-Module/dp/B00E1GGE40?tag=googinhydr18418-21&tag=googinkenshoo-21&ascsubtag=2a6ca201-f55d-43ad-af12-dcfd500d164b)
* [USB Microphone](https://www.amazon.in/gp/product/B06VWBYVVP/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1)
* [GPS module](https://www.ebay.in/itm/331757723713?aff_source=Sok-Goog)
* [RFID reader](https://www.amazon.in/Keychain-RC522-Sensor-Module-Fudan/dp/B00MP4CN2C?tag=googinhydr18418-21&tag=googinkenshoo-21&ascsubtag=2a6ca201-f55d-43ad-af12-dcfd500d164b)
* [RaspberryPi Model-3B](https://www.amazon.in/RASPBERRY-MODEL-INBULT-BLUETOOTH-Wifi/dp/B01G882L3G/ref=sr_1_2?s=industrial&ie=UTF8&qid=1522333204&sr=1-2&keywords=raspberry+pi+3+kit)



# Getting Started #

We are giving stepwise instructions for developing Coco from scratch! ***<u>Don't forget to check the Wiki Tab.</u>***

* [Initialising the Pi](https://github.com/abhimanyu-bitsgoa/Coco/wiki/Initialising-the-Pi)
* [Adding Face recognition](https://github.com/abhimanyu-bitsgoa/Coco/wiki/Camera)
* [Adding Voice recognition](https://github.com/abhimanyu-bitsgoa/Coco/wiki/Voice)
* [Adding GPS](https://github.com/abhimanyu-bitsgoa/Coco/wiki/GPS-Module)
* [Adding RFID](https://github.com/abhimanyu-bitsgoa/Coco/wiki/RFID)
* [Helper Scripts](https://github.com/abhimanyu-bitsgoa/Coco/wiki/Asgard:-SSH-tunnel-for-Pi)
* [Setting MongoDB](https://github.com/abhimanyu-bitsgoa/Coco/wiki/MongoDB)
* [Pin Diagram](https://drive.google.com/file/d/1cki_2bnYLimEntTy9uSepCbNUCva041G/view)



## Running the code ##

* Clone the repository.
* `cd Coco/main_scripts/`
* `sudo su`
* `./run_coco.sh`
* Now follow the voice instructions given by the Pi. ( Wake up word "**Coco**")



## Understanding the Code ## 

We have designed this project in accordance with smart software paradigms to increase the maintainability of our code base. Some of the salient feature of the project are:

* A completly modular approach. All the features are completely separated out into logical modules to ease management and curb redundancy.
* We have used Open Source tools for most of our tasks and nearly all our tools are developed just with basic python libraries.
* We have kept the OS calls to the minimum while calling various internal scripts, rather we fiddled with the source code of the base libraries to directly use them.
* Please check the [flow diagram](https://drive.google.com/file/d/1a9uC6f2SoihsYGOX5DaV4x78eyz1eieF/view) to see how things work together.



## Interview with the Developers ##

**Q.** *Does the project work and solve the problem it is aimed at?*

**A.** Yes! Coco can successfully detect a person and make an entry into the database along with the location and timestamp, thereby solving the original problem use case. Additionally we were able to integrate **Joke**, **News** and **Dictionary** feature in the month's time frame all using just basic python libraries.

**Q.** *Did you take care of the user experience and maintainable code?*

**A.** Like we said, developing Coco was tough but we always kept people who will be using it and people who will be developing it in our minds.
Since the product is supposed to be used on car's dashboards, therefore we made it completely headless, and the entire Pi will be controlled by voice, giving out verbose instructions to the user.Also we used modular approach in designing this code, so that maintenence is easier later on.

**Q.** *Is your solution feasible for production?*

**A.** Right from the prototyping phase, we paid special attention towards the cost and the scalability of our application. We questioned ourself at every step of the project as to whether the current feature will be able to perfrom well when it will come to production. For instance,**This is the main reason why we have not used any ready made voice assistants available in the market and decided to use simple python STT library to build our project.** So straight from the prototyping phase we pictured our product for production and worked accordingly.Also with small tweaks in the code, **our product can scale up to multicore architecture ( Camera module ).**

**Q.** *So what next ?*

**A.** In the course of the hackathon we have developed an independent open source python bases voice assistant that is easy to setup and work with. Therefore we are planning to develop it further with richer set of feature and since the code is modular any additional new features can be added pretty easily.



##  Challenges faced ##

***Challenge:*** The image files required for the face recognition allocates huge amount of memory for a portable device.

***Solution:*** We converted images to .npy arrays and used them directly and we were able to achieve a compression rate of ***<u>95%</u>*** per file ( from 18 KB to 1 KB )

***Challenge:*** Our entire SD card got corrupted a week before.

***Solution:*** We developed proper documentation and automated scripts to get back with the full installation in a short span of time. Additionally we will be developing a master script that will install the entire codebase with a single command, taking care of all the dependencies.

***Challenge***:  The hardware devices were not communicating with each other properly.

***Solution:*** We gained a deep understanding of Raspberry Pi and various modules before interfacing them with each other and didn't put much load on the CPU by efficient coding style ( For instance, Avoiding system calls wherever possible). Also we gained knowledge about serial port manipulation, configuration files and raspbian environment while completing the project.

***Challenge***: Limited computational resources on Raspberry Pi.

***Solution:*** We had to gracefully shutdown all the zombie resources in the system, to keep up with the performance on the system.



## Team ##

* [Abhimanyu Singh Shekhawat](https://www.linkedin.com/in/abhimanyubitsgoa/)
* [Jainam Shah](https://www.linkedin.com/in/shahjainam023/)
* [GV Sandeep](https://www.linkedin.com/in/greetsandeep/)

