# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

$scriptInflux = <<SCRIPT
wget -qO - https://packages.elasticsearch.org/GPG-KEY-elasticsearch | sudo apt-key add -
sudo add-apt-repository "deb http://packages.elasticsearch.org/elasticsearch/1.4/debian stable main"

sudo apt-get update
sudo apt-get -y upgrade

wget http://s3.amazonaws.com/influxdb/influxdb_latest_amd64.deb
sudo dpkg -i influxdb_latest_amd64.deb
sudo /etc/init.d/influxdb start

sudo apt-get -y install git nodejs python python-setuptools
cd /opt
sudo git clone https://github.com/etsy/statsd.git
cd statsd
sudo apt-get -y install npm
sudo npm install statsd-influxdb-backend -d
sudo cp /vagrant/config.js config.js

sudo apt-get -y install apache2
wget http://grafanarel.s3.amazonaws.com/grafana-1.9.1.tar.gz
tar xvf grafana-1.9.1.tar.gz
sudo mv grafana-1.9.1/ /var/www/html/grafana
cd /var/www/html/grafana
sudo cp /vagrant/config.grafana.js config.js

# Install ElasticSearch
# Install ElasticSearch
sudo apt-get -y install openjdk-7-jre elasticsearch
sudo update-rc.d elasticsearch defaults 95 10
sudo /etc/init.d/elasticsearch start

# Install Kibana
cd ~
wget https://download.elasticsearch.org/kibana/kibana/kibana-4.0.1-linux-x64.tar.gz
tar xvf kibana-4.0.1-linux-x64.tar.gz
sudo mv kibana-4.0.1-linux-x64/ /opt/kibana
sudo cp /vagrant/kibana.sh /etc/init.d/kibana
sudo /etc/init.d/kibana start

# Create two databases: demo and dash
curl -X POST 'http://localhost:8086/db?u=root&p=root' -d '{"name": "demo"}'
curl -X POST 'http://localhost:8086/db?u=root&p=root' -d '{"name": "dash"}'

# start stats service
sudo cp /vagrant/statsd /etc/init.d/
sudo chmod +x /etc/init.d/statsd
sudo update-rc.d statsd defaults
sudo /etc/init.d/statsd start

SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.
  # config.vbguest.auto_update = false
  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "ubuntu/trusty64"
  config.vm.provider "virtualbox" do |vb|
    # Don't boot with headless mode
    # vb.gui = true
    vb.memory = 1024
    vb.cpus = 2
  end
  config.vbguest.auto_update = false
  config.vm.provision "shell", inline: $scriptInflux

  config.vm.network :forwarded_port, guest: 8125, host: 8125
  config.vm.network :forwarded_port, guest: 8083, host: 8083
  config.vm.network :forwarded_port, guest: 8086, host: 8086
  config.vm.network :forwarded_port, guest: 8090, host: 8090
  config.vm.network :forwarded_port, guest: 8099, host: 8099
  config.vm.network :forwarded_port, guest: 80, host: 8080

  config.vm.network "private_network", ip: "192.168.50.2"
end
