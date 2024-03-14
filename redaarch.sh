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

arch-chroot /mnt ./inside-chroot.sh


	


############################################################
## Last thing to do is a bit of mounting cleanup
############################################################
umount -R /mnt/boot
umount -R /mnt
reboot
