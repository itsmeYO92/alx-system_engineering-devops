#this puppet script executes a command
exec { 'kill':
    command => '/bin/pkill -f "killmenow"',
}
