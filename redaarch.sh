############################################################
## This is my own arch install script 
## It is a minimal one since all customization is done
## through my dotfiles' install.sh
############################################################


# making the font get bigger
# echo "this is the font before:"
# sleep 3
# setfont ter-132b
# echo "this is the font after"
# sleep 3
# clear

# set up the time
echo "configuring the time has begun"
sleep 3
timedatectl
timedatectl set-ntp true
timedatectl set-timezone Africa/Casablanca
echo "setting up the time has finished"
sleep 3
clear

# updating keyrings
echo "updating the keyrings "
sleep 3
pacman -Sy --needed --noconfirm archlinux-keyring
echo "just updated the keyring for arch \nwhatever that means!"
sleep 3
clear


############################################################
###  Disk Partitionning 
############################################################

# $ parted [options] [device [command [options...]...]]
echo "partitionning the disk"
sleep 3
lsblk
DISK="here goes the disk"
read -p "enter the disk name in here, pay attention to typos" DISK
# use parted
parted $DISK --script mklabel gpt
parted $DISK --script mkpart fat32 1MiB 301MiB
parted $DISK --script set 1 esp on
parted $DISK --script mkpart ext4 301MiB 100%
# making the file system -- formatting
mkfs.fat -F 32 ${DISK}1
mkfs.ext4 ${DISK}2
# mounting the partitions
mount ${DISK}2 /mnt
mount --mkdir ${DISK}1 /mnt/boot


############################################################
### before chrooting
############################################################
# generating the fstab file
echo "generating the fstab file "
sleep 2
genfstab -U /mnt >> /mnt/etc/fstab
# chrooting to the life env
echo "installing software"
pacstrap -K /mnt base linux linux-firmware intel-ucode networkmanager
sleep 2

arch-chroot /mnt 


############################################################
### Setting up users
############################################################
# setting the password for the root user
echo root:Tzbg5340 | chpasswd
# adding a new user
useradd -m reda --shell /bin/bash
echo reda:1966 | chpasswd

############################################################
### Performing menial tasks 
############################################################
# setting up the timezone
echo "setting up the timezone"
sleep 3
ln -sf /usr/share/zoneinfo/Africa/Casablanca /etc/localtime
# syncing the system to hardware clock
echo "syncing the system to hardware clock"
sleep 3
hwclock --systohc
# setting up the locale
echo "setting up the locale"
sleep 3
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
locale-gen
# setting up the language
echo "setting up the language"
sleep 3
echo "LANG=en_US.UTF-8" > /etc/locale.conf
# host name stuff
echo "host name stuff"
sleep 3
echo homeworld16 > /etc/hostname
echo "127.0.0.1 localhost" >> /etc/hosts
echo "::1       localhost" >> /etc/hosts
echo "127.0.1.1 archmc.localdomain archmc" >> /etc/hosts


############################################################
###  Systemd-boot setup
############################################################
bootctl --path=/boot install
uuid=blkid  $DISK | awk '{print $2}'
touch /boot/loader/entries/arch.conf
echo "title Arch Linux" >> /boot/loader/entries/arch.conf
echo "linux /vmlinuz-linux" >> /boot/loader/entries/arch.conf
echo "initrd  /intel-ucode.img" >> /boot/loader/entries/arch.conf
echo "initrd /initramfs-linux.img" >> /boot/loader/entries/arch.conf
echo "options root=$uuid rw" >> /boot/loader/entries/arch.conf

echo "default arch" >  /boot/loader/loader.conf
echo "timeout 4" >>  /boot/loader/loader.conf
echo "console-mode max" >>  /boot/loader/loader.conf
echo "editor no" >>  /boot/loader/loader.conf

bootctl --path=/boot update
	


############################################################
## Last thing to do is a bit of mounting cleanup
############################################################
exit
umount -R /mnt/boot
umount -R /mnt
reboot
