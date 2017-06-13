#!/usr/bin/env bash
export DATE="2017-06-12"

echo "Restore Redmine Instance Dez VI - IT"
sudo -u postgres dropdb --if-exists -U postgres redmine_dez_vi
sudo -u postgres createdb -O redmine -U postgres -E UTF-8 redmine_dez_vi
sudo rm -r /data/redmine/dez_vi/*

sudo tar --gzip --extract --directory=/data/redmine/dez_vi --file=/home/ansible/backup/${DATE}_redmine_ref-vi.4_files.tar.gz      
gunzip -c /home/ansible/backup/${DATE}_redmine_ref-vi.4_db.sql.gz | sudo -u postgres psql redmine_dez_vi


echo "Restore Redmine Instance Webprojekte (Ref. VI.5)"
sudo -u postgres dropdb --if-exists -U postgres redmine_vi5_webprojekte
sudo -u postgres createdb -O redmine -U postgres -E UTF-8 redmine_vi5_webprojekte
sudo rm -r /data/redmine/webprojekte/*

sudo tar --gzip --extract --directory=/data/redmine/webprojekte --file=/home/ansible/backup/${DATE}_redmine_ref-vi.5_files.tar.gz    
gunzip -c /home/ansible/backup/${DATE}_redmine_ref-vi.5_db.sql.gz | sudo -u postgres psql redmine_vi5_webprojekte


echo "Restore Redmine Instance Dez VII - Haushalt"
sudo -u postgres dropdb --if-exists -U postgres redmine_dez_vii
sudo -u postgres createdb -O redmine -U postgres -E UTF-8 redmine_dez_vii
sudo rm -r /data/redmine/dez_vi/*

sudo tar --gzip --extract --directory=/data/redmine/dez_vii --file=/home/ansible/backup/${DATE}_redmine_dez-vii_files.tar.gz      
gunzip -c /home/ansible/backup/${DATE}_redmine_dez-vii_db.sql.gz | sudo -u postgres psql redmine_dez_vii


sudo chown -R redmine:redmine /data/redmine/
echo "Restore Complete"