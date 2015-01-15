## Background
I wanted to use statsd to collect metrics on my local machine. And, I wanted a good front-end to view the metrics on a dashboard. After a good amount of failure, I found [this article](http://www.symantec.com/connect/blogs/metrics-cocktail-statsdinfluxdbgrafana)

## Usage

### Clone this repo

```bash
git clone https://github.com/curtismitchell/vagrant-statsd-grafana.git
```

### Vagrant up
```bash
cd vagrant-statsd-grafana
vagrant up
```

### Visit your grafana page
Open [http://localhost:8083/grafana](http://localhost:8083/grafana) and configure your dashboard.
