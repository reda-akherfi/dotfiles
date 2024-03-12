######################################################################
######################################################################
###### This script is going to be completed bit by bit
###### as I am setting up my working env
######################################################################
######################################################################


######################################################################
### General Settings
######################################################################
username=reda

######################################################################
### Installing my favorite software
######################################################################
# my go to text editor [more like a lifestyle]
pacman -Sy vim   
# zathura with epub, pdf ... support
pacman -Sy zathura zathura-pdf-mupdf  
# vifm is a cozy file manager for a vim user
pacman -Sy vifm

######################################################################
### Creating Symlinks for dotfiles and such
######################################################################
ln -sf /home/$username/dotfiles/.vimrc /home/$username/.vimrc
ln -sf /home/$username/dotfiles/.bashrc /home/$username/.bashrc
ln -sf /home/$username/dotfiles/.config/zathura /home/$username/.config/zathura
ln -sf /home/$username/dotfiles/.config/vifm /home/$username/.config/vifm

