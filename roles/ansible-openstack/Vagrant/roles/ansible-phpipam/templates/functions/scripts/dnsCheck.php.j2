<?php

  // include required scripts
  require_once( dirname(__FILE__) . '/../functions.php' );
  require_once( dirname(__FILE__) . '/../functions-mail.php');
  require_once( dirname(__FILE__) . '/../scan/config-scan.php');

  // config
  $email = true;                  //set mail with status diff to admins
  $emailText = false;             //format to send mail via text or html

  $settings = getAllSettings();
  // Since we're re-using this function, this script is also dependent on the following condition
  // pingSubnet == 1 && excludePing != 1
  $existing = getAllIPsforScan(true);
  $updated = array();

  // $existing format
  // [index] => Array
  //   (
  //       [id] => ####
  //       [description] => xxxx
  //       [subnetId] => #
  //       [ip_addr] => #########
  //       [dns_name] => xxxx
  //       [lastSeen] => yyyy-mm-dd hh:mm:ss
  //       [oldStamp] => yyyy-mm-dd hh:mm:ss
  //   )

  foreach($existing as $ip) {
    // Lookup current DNS entry
    $dns_name = ResolveDnsName ($ip['ip_addr']);
    // Array
    // (
    //   [class] => resolved
    //   [name] => xxxxx
    // )
    // Compare it with the current value in the DB
    if ($ip['dns_name'] != $dns_name['name']) {
      // Perserve old entry for reporting purposes
      $ip['old_dns_name'] = $ip['dns_name'];
      // Update entry
      $ip['dns_name'] = $dns_name['name'];
      @updateDNSName($ip);
      // Store record for reporting
      $updated[] = $ip;
    }
  }

   if(sizeof($updated)>0 && $email) {
    //send text array, cron will do that by default if you don't redirect output > /dev/null 2>&1
    //this will be unformated (i.e. no Transform2long on the ip_addr field)
    if($emailText) {
      print_r($updated);
    }
    //html
    else {
      $mail['from']     = "$settings[siteTitle] <ipam@$settings[siteDomain]>";
      $mail['headers']  = 'From: ' . $mail['from'] . "\r\n";
      $mail['headers'] .= "Content-type: text/html; charset=utf8" . "\r\n";
      $mail['headers'] .= 'X-Mailer: PHP/' . phpversion() ."\r\n";

      //subject
      $mail['subject']  = "phpIPAM updated DNS ".date("Y-m-d H:i:s");

      //header
      $html[] = "<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.01 Transitional//EN' 'http://www.w3.org/TR/html4/loose.dtd'>";
      $html[] = "<html>";
      $html[] = "<head></head>";
      $html[] = "<body>";
      //title
      $html[] = "<h3>phpIPAM updated ".sizeof($updated)." DNS values</h3>";
      //table
      $html[] = "<table style='margin-left:10px;margin-top:5px;width:auto;padding:0px;border-collapse:collapse;border:1px solid gray;'>";
      $html[] = "<tr>";
      $html[] = " <th style='padding:3px 8px;border:1px solid silver;border-bottom:2px solid gray;'>IP</th>";
      $html[] = " <th style='padding:3px 8px;border:1px solid silver;border-bottom:2px solid gray;'>Old Hostname</th>";
      $html[] = " <th style='padding:3px 8px;border:1px solid silver;border-bottom:2px solid gray;'>New Hostname</th>";
      $html[] = " <th style='padding:3px 8px;border:1px solid silver;border-bottom:2px solid gray;'>Subnet</th>";
      $html[] = " <th style='padding:3px 8px;border:1px solid silver;border-bottom:2px solid gray;'>Section</th>";

      $html[] = "</tr>";
      //Changes
      foreach($updated as $index) {
        //set subnet
        $subnet = getSubnetDetails($index['subnetId']);
        $subnetPrint = Transform2long($subnet['subnet'])."/".$subnet['mask']." - ".$subnet['description'];
        //set section
        $section = getSectionDetailsById($subnet['sectionId']);
        $sectionPrint = $section['name']." (".$section['description'].")";

        $html[] = "<tr>";
        $html[] = " <td style='padding:3px 8px;border:1px solid silver;'>".Transform2long($index['ip_addr'])."</td>";
        $html[] = " <td style='padding:3px 8px;border:1px solid silver;'>".$index['old_dns_name']."</td>";
        $html[] = " <td style='padding:3px 8px;border:1px solid silver;'>".$index['dns_name']."</td>";
        $html[] = " <td style='padding:3px 8px;border:1px solid silver;'><a href='$settings[siteURL]".create_link("subnets",$section['id'],$subnet['id'])."'>$subnetPrint</a></td>";
        $html[] = " <td style='padding:3px 8px;border:1px solid silver;'><a href='$settings[siteURL]".create_link("subnets",$section['id'])."'>$sectionPrint</a></td>";//

        $html[] = "</tr>";
      }
      $html[] = "</table>";
      //footer

      //end
      $html[] = "</body>";
      $html[] = "</html>";

      //save to array
      $mail['content'] = implode("\n", $html);

      //send to all admins
      sendStatusUpdateMail($mail['content'], $mail['subject']);
    }
  }
?>