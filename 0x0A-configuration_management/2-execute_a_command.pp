#this puppet script installs the package flask from pip3
exec { 'kill':
    command => 'pkill -f killmenow',
    path    => ['usr/bin', '/usr/sbin'],
}
