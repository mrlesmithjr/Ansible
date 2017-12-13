# Configure the PowerDNS provider
provider "powerdns" {
  api_key = "${var.pdns_api_key}"
  server_url = "${var.pdns_server_url}"
}
