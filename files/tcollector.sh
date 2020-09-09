#!/bin/sh

#tutaj znajdowane sa metryki z dopiskiem _incomming, _outgoing , _bridge
/usr/bin/v3xmlSHMDump -d /v3xml0 -f etc/ipc.shm  | grep mic5 | sed -e "s/VXML|mic5|/v3xml0./g" >> /tmp/tcollector_svi2
/usr/bin/v3xmlSHMDump -d /v3xml1 -f etc/ipc.shm  | grep mic5 | sed -e "s/VXML|mic5|/v3xml1./g" >> /tmp/tcollector_svi2
/usr/bin/v3xmlSurvMemBrowser-multi.ksh | grep kbmemusedv3xml | sed -e "s/VXML|//g" >> /tmp/tcollector_svi2

#wyciaganie z logow , chyba chodzi o puste polaczenia (/bin/grep "OC\|IC" /var/log/messages )
echo `/LIBRE/etc/qos_empty_record.sh | cut -d"." -f1` "percomblanche" >> /tmp/tcollector_svi2

#Rozmowa z Clemaint  , mozna wywalic badz zastapic sensowniejszym rozwiazaniem
#zbieranie informacji ztop (/usr/bin/top -b -n 1 | /bin/grep audioCapture| /bin/cut -d"o" -f2- | /usr/bin/tr -s ' ' |/bin/cut -d" " -f8
echo `/LIBRE/etc/survCPUAudioCapture.ksh | cut -d"." -f1` "perCPUaudioCapture" >> /tmp/tcollector_svi2

#dane z ps , po rozmowie  z Clemant mozna to usunac
#The Virtual Set Size is a memory size assigned to a process ( program ) during the initial execution. The Virtual Set Size memory is sim#ply a number of how much memory a process has available for its execution. 
echo `/LIBRE/etc/survMemAudioCapture.ksh | cut -d"." -f1` "kbmemusedaudioCapture" >> /tmp/tcollector_svi2

#kolejna tabelka , mozna uzyc Regeksow python
/usr/bin/cxiSHMDump -d /ccxml0 | grep "CXI|" | sed -e "s/CXI|/ccxml/g" >> /tmp/tcollector_svi2


#duza tabela kilka metryk , z opcja -b zrzuca tylko liczby, pierwsza najmniejsza podaje ilosc aktywanych polaczen. Tylko ta nas interesuje
echo `/LIBRE/etc/nb_audiocapture.sh` "nbaudiocapture" >> /tmp/tcollector_svi2


#zbiera ostania linie z wyniku , liczba wskazuje ilosc konferencji
echo `/LIBRE/etc/nb_confsrv.sh` "nbconfsrv" >> /tmp/tcollector_svi2

chmod 777 /tmp/tcollector_svi2
#petla wyszukuje w poprzednich wynikach metryk z dopiskiem _incoming, _outgoing, _bridge. Jesli nie znajdzie pobiera liste aplikacji ze zmiennej list, 
#dopisuje do itemu z listy dopisek i wrzuca kolejno  do pliku /tmp/tcollector_svi2 . Lista jest bardzo dluga... 

list=`grep "<app id=" /etc/v3xml/applist.xml | cut -d'"' -f2`
for i in $list
do
        incoming=$(grep -c ${i}_incoming /tmp/tcollector_svi2)
        bridge=$(grep -c ${i}_bridge /tmp/tcollector_svi2)
        outgoing=$(grep -c ${i}_outgoing /tmp/tcollector_svi2)
        if [ $incoming -eq 0 ]
        then
                echo "0 ${i}_incoming" >> /tmp/tcollector_svi2
        fi
        if [ $outgoing -eq 0 ]
        then
                echo "0 ${i}_outgoing" >> /tmp/tcollector_svi2
        fi
        if [ $bridge -eq 0 ]
        then
                echo "0 ${i}_bridge" >> /tmp/tcollector_svi2
        fi
done

mv /tmp/tcollector_svi2 /tmp/tcollector_svi 
