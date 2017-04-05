# 3dr-SOLO-QR-recognition

# Initialization:
in order to establish connection with the Solo, follow this guide: http://dev.3dr.com/starting-network.html
Genrally much information can be found in the official above mentioned 3dr development guide, but there things there that doesn't actually work as would be specified ahead, so be wary.

# Extendind the root partition size:
The Solo comes with about 90 MB in the root parition, not much to work with. 3dr provides a command line tool which is called CLI, which enables installing python packages on the solo and running scripts. It can be found here: http://dev.3dr.com/starting-utils.html
CLI also includes a tool for automatically resize the root parition to about 600 MB. However, this tool doesn't work properly and may hang or even damage the software, forcing you to make a factory reset (https://3dr.com/support/articles/208396933/factory_reset/ - note that after reseting the device you have to pair it with the controller. Follow the instructions on the controller). The solution is to try and execute the resizing script manually, line by line - it worked for me. The script can be found here: https://github.com/3drobotics/solo-cli/blob/master/soloutils/resize.py

# Connecting Solo to the Internet:
Again, use the CLI to do that - http://dev.3dr.com/starting-utils.html

# Installing packages:
Follow 3dr's dev guide to install basic packages using the CLI. The Solo supports initially only python 2.7 scripts, but after all it runs linux (Yocto distro) so a gcc compiler can also be installed manually. You can use these commands (from the solo itself after it went online):

smart channel --remove cortexa9hf_vfp_neon -y
smart channel --remove cortexa9hf_vfp_neon_mx6 -y
smart channel --add cortexa9hf_vfp_neon type=rpm-md baseurl=http://downloads.yoctoproject.org/releases/yocto/yocto-1.5.1/rpm/cortexa9hf_vfp_neon/ -y
smart channel --add cortexa9hf_vfp_neon_mx6 type=rpm-md baseurl=http://downloads.yoctoproject.org/releases/yocto/yocto-1.5.1/rpm/cortexa9hf_vfp_neon_mx6/ -y
smart update
smart install gcc gcc-symlinks libc6-dev gcc-dev binutils python-dev gstreamer-dev -y

# Getting access to the video stream
By default Solo streams the video from the GoPro it uses only to the app (search for "3dr solo" in google play or appstore). The CLI provides a tool that is supposed to grant access to the stream to scripts (instead of the app, it's unable to stream to two places at once), only that this tool was found out by users to be outdated, as it uses an architecture Solo now longer possesses. You can read all about it at https://discuss.dronekit.io/t/solo-video-acquire-please/320/12
Many users have tried to figure out a way to gain access to the video without using 3dr's tool. The link above contains very helpful discussions and ways to try and do so. The most trivial way to gain access to the video is to navigate (on the Solo itself) to the /etc folder, open (edit using vi) the file etc/inittab and comment out "VID:4:respawn:vidlaunch", then reboot the Solo. After that you can access the camera (for instance like I did in the scripts here). See https://discuss.dronekit.io/t/solo-video-acquire-please/320/32 for info about building your own pipeline or even trying to split the pipeline. Don't forget to undo the change in the inittab file of you want to restore the video stream to the app.

# Recognizing QR Codes
The ZBar library (http://zbar.sourceforge.net/) eanbles to recognize codes from camera stream or images. I've tried to build it from source on the Solo itself, in order to use Solo's computer power to make the media analysis on the fly without loosing quality to transmission, not to mention time lag. However, I've encountered difficulties doing so, partly due to many dependencies Zbar needs, and partly due to some Linux issues over building I couldn't resolve (the ./config script does something strange that the build script doesn't like). Note that you can save the need to install many of the dependencies by disabling some of ZBar's features during configuraion, see their documentation for that.
What I enetually did was taking pictures every two seconds and sending it over to my computer, which uses Zbar locally to detect and recognize the code.

# The scripts here - instructions
First ssh to Solo, and transport there the qrdetect.py script. In another instance of a terminal run the script copyimg, which copies the captured frame every two seconds (it is a problem to connect from A to B using ssh and in the same session download files from B to A, thus the seperate session). Now run on your computer the chcode.py script. Make sure all the pathes suit each other, and put the car license plate number you seek in the right place in the script.
