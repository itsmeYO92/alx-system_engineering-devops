#this puppet script installs the package flask from pip3
package { 'flask':
    provider => 'pip3',
    ensure  => '2.1.0',
}
