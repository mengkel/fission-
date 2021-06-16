# fission reaction data
This repo will demonstrate how to add fission reactions to the existing reaction network in xml file\
\
**cd nucnet-tools-code/data_pubb**\
\
First, we should use python to create a **new_reaction_data.xml**, which is uploaded above. \
\
Then, we need to libnucnet examples: to check the new file:\
\
**../libnucnet/print_reactions new_reaction_data.xml**\
\
Now, we use [Xinclude](https://sourceforge.net/u/mbradle/blog/2014/12/including-xml-in-other-libnucnet-xml/) to include the fission data in the network data. We use the file below to write a file net_with_fission.xml with the lines

```javascript
<?xml version="1.0" encoding="ISO-8859-1"?>

<nuclear_network
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:xi="http://www.w3.org/2001/XInclude"
  xsi:schemaLocation="http://libnucnet.sourceforge.net/xsd_pub/2019-01-15/libnucnet__net       http://libnucnet.sourceforge.net/xsd_pub/2019-01-15/libnucnet__net.xsd"
>

   <!-- Nuclear data -->

   <nuclear_data>
        <xi:include href="my_net.xml" xpointer="xpointer(//nuclide)"/>
   </nuclear_data>

   <!-- Reaction data -->

   <reaction_data>
      <xi:include href="my_net.xml" xpointer="xpointer(//reaction)"/>
      <xi:include href="fission.xml" xpointer="xpointer(//reaction)"/> 
   </reaction_data>

</nuclear_network>

```
Once we have created this file, we first validate it by typing:\
\
**xmllint --noout --xinclude --schema http://libnucnet.sourceforge.net/xsd_pub/2019-01-15/libnucnet__net.xsd net_with_fission.xml**
\
This should return the line:\
\
**net_with_fission.xml validates**\
\
Since we have a valid XML file, we can proceed. type\
\
**../libnucnet/print_reactions net_with_fission.xml**\
\
This prints out all the nuclei. Since we want to check that we are including the fission reactions, We need to use an XPath expression to them. type\
\
**../libnucnet/print_reactions net_with_fission.xml "[source[contains(.,'fission')]]"**\
\
This shows the fission reactions in the network file. We can check that the reactions are valid (conserve baryon number, charge, and lepton number) by typing\
\
**../libnucnet/print_valid_reactions net_with_fission.xml "" "[source[contains(.,'fission')]]"**\
\
To prepare the calculation, We now edit the file zone.xml, which is also uploaded above.\
\
Now, in my palmetto account, I will do\
\
**export WN_USER=1** to minimize the running time\
\
Then I go the appropriate folder\
\
**cd nucnet-tools-code/my_examples/network**\
\
I set the environment variable\
\
**export NNT_USE_SPARSKIT2=1**\
\
and cleaned and remade the code\
\
**make clean**\
\
**make all_network**\
\
Once this step is done\
\
**./run_single_zone ../../data_pub/net_with_fission.xml ../../data_pub/zone.xml my_output.xml "[z <= 90]"**\
\
We also need to run a calculation without fission. \
\
**./run_single_zone ../../data_pub/my_net.xml ../../data_pub/zone.xml my_output_no_fission.xml "[z <= 90]"**\
\
Or, we can use\
\
**qsub **.pbs**\
\
Then we can use wnutils to plot the final abunds and compare the difference.


