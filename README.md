# VlcNote

This plugin is meant for writing notes along with a video playing

## Installation

Use your plugin manager of choice.

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/nanoseb/VlcNote ~/.vim/bundle/VlcNote`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Bundle 'https://github.com/nanoseb/VlcNote'` to .vimrc
  - Run `:BundleInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'https://github.com/nanoseb/VlcNote'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'https://github.com/nanoseb/VlcNote'` to .vimrc
  - Run `:PlugInstall`

## Available functions

* `RunVlc`: to run vlc with the appropriate parameters (telnet), if the current
filename is also the name of a video file (with a different extension), this
command will open this video.
One can also run vlc with the following arguments:

`    vlc --extraintf telnet --telnet-password passwordVLC --telnet-port 4212 file.mp4`

* `PauseVlc`: to pause and play the video 
* `WriteTimestampVlc`: write the current timestamp at the begining of the line
* `GotoTimestampVlc`: play the video at the line timestamp


