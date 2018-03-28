#!/bin/bash
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

echo "${green}1. Preparing the hosts file..."
rm hosts
cp hosts.default hosts

echo ""
echo "2. Running ansible to create AWS instances for Ops Manager and Replica Set..."
echo "${reset}Check the log at logs/ansible-aws.log"
ansible-playbook -i hosts playbooks/ansible-aws.yml > logs/ansible-aws.log

SORTIDA=$?
if [ "$SORTIDA" -eq 0 ];
then
    echo "${green}OK creating the AWS instances"
    echo ""
    echo "3. Adjusting hosts file with the AWS instance names..."
    python addNewHosts.py > logs/addNewHosts.log

    echo ""
    echo "4. The hosts file has been modified and this is how it looks now:"
    echo "${reset}"
    cat hosts

    echo "${green}"
    read -rsp $'5. If the file looks OK (all vars have values and all Replica Set members are listed) press any key to continue...\n' -n1 key
    echo ""
    echo "6. Installing Ops Manager"
    echo "${reset}Check the log at logs/ansible-install-om.log"
    ansible-playbook -i hosts playbooks/ansible-install-om.yml > logs/ansible-install-om.log

    SORTIDA=$?
    if [ "$SORTIDA" -eq 0 ];
    then
        echo "${green}OK installing Ops Man"
        echo ""
        om_url=`grep "opsmanagerurl=" hosts| head -1| sed 's/opsmanagerurl=/mms.centralUrl=/'`
        echo $om_url >> files/parameters_om.config

        echo "8. Configure OM"
        echo "${reset}Check the log at logs/ansible-config-om.log"
        ansible-playbook -i hosts playbooks/ansible-config-om.yml > logs/ansible-config-om.log

        SORTIDA=$?
        if [ "$SORTIDA" -eq 0 ];
          then
            echo "${green}Ops Manager has been configured successfully"
            echo ""

            echo "$reset"
            tail -2 hosts
            read -rsp $'Login to OM web UI and add OM server IP to the Whitelist. Then return here and press any key to continue...\n' -n1 key

            echo "9. Onboard Replica Set"
            echo "${reset}Check the logs at logs/ansible-onboard-rs.log"
            ansible-playbook -i hosts playbooks/ansible-python.yml > logs/ansible-onboard-rs.log

            SORTIDA=$?
            if [ "$SORTIDA" -eq 0 ];
              then
                echo "${green}Replica Set was onboarded successfully"
                echo ""
              else
                echo "${red}Oups! There was a problem onboarding Replica Set. Check  logs/ansible-onboard-rs.log for more details"
                echo "Configure BACKUP before loading any data to your database!!!"
            fi
          else
            echo "${red}There was a problem configuring Ops Manager. Check  logs/ansible-config-om.log for more details"
          fi
    else
        echo "${red}Failed to install Ops Man"
        exit
    fi

else
    echo "${red}Failed to create AWS instances"
fi
