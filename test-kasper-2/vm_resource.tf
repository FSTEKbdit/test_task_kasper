
terraform {
  required_providers {
    vagrant = {
      source = "bmatcuk/vagrant"
    }
  }
}
provider "vagrant" {}
resource "vagrant_vm" "alma" {
  name            = "alma9"
  vagrantfile_dir = "./"
  get_ports       = true
}