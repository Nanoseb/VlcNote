" --------------------------------
" Add the plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))
python from VlcNote import VlcNote

" ---------------------------
"  Functions
" ---------------------------

function! WriteTimestamp()
python << endPython

vlc = VlcNote()
vlc.write_timestamp()
vlc.logout()

endPython
endfunction


function! GotoTimestamp()
python << endPython

vlc = VlcNote()
vlc.goto_timestamp()
vlc.logout()

endPython
endfunction


function! Pause()
python << endPython

vlc = VlcNote()
vlc.pause()
vlc.logout()

endPython
endfunction

function! RunVlc()
python << endPython
import subprocess
import glob

path = vim.eval("expand('%:p:r')")
videoext = ("mp4", "mkv", "avi", "webm", "flv")

args = ["vlc", "--extraintf", "telnet", "--telnet-port", "4212", "--telnet-password", "passwordVLC"]
for file in glob.glob(path+"*"):
    if file.endswith(videoext):
        args.append(file)
        break

with open(os.devnull, 'w') as devnull:
    subprocess.Popen(args, stdout=devnull, stderr=devnull)


endPython
endfunction
" ----------------------------
"  Expose commands to the user
" ----------------------------

command! WriteTimestampVlc call WriteTimestamp()
command! GotoTimestampVlc call GotoTimestamp()
command! PauseVlc call Pause()
command! RunVlc call RunVlc()
