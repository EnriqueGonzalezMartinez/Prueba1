#!/bin/bash

var=$(cat /etc/*-release | grep ID=)
# This if verifies that the OS is centos and the version is 7
if [[ $var == *'ID="centos"'* && $var == *'VERSION_ID="7"'* ]]
then
	echo "One CentOS 7 was identified."
	# This "if" checks if there is any ClamAV package installed to uninstall it.
	if [[ -n $(yum list installed | grep clamav) ]]
	then
		sudo yum -y remove clamav*
	fi
	# Install the ClamAV and Epel packages
	sudo yum install -y https://www.clamav.net/downloads/production/clamav-0.104.1.linux.x86_64.rpm
	sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
	# Update all packages
	sudo yum -y update
# This if verifies that the OS is centos and the version is 8
elif [[ $var == *'ID="centos"'* && $var == *'VERSION_ID="8"'* ]]
then
	echo "One CentOS 8 was identified."
	# This "if" checks if there is any ClamAV package installed to uninstall it.
	if [[ -n $(yum list installed | grep clamav) ]]
	then
		sudo yum -y remove clamav*
	fi
	# Install the ClamAV package
	sudo yum install -y https://www.clamav.net/downloads/production/clamav-0.104.1.linux.x86_64.rpm
	# Update all packages
	sudo yum -y update

else
	echo "The operating system is not a Centos"
fi
