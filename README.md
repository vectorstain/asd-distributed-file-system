# asd-distributed-file-system
https://ipfscluster.io/documentation/quickstart/

# Guida al funzionamento di IPFS

Progetto ASD A.A. 2022-23
Realizzato da: 
Federico Fiorio 
Vincenzo Maria Calandra

# Struttura dell'infrastruttura
Come abbiamo illustrato, la nostra rete è composta da ipfs-cluster e ipfs.
Una macchina IPFS che accede all'interno della rete si aggancia ad un IPFS-CLUSTER che gli fornisce la struttura di parte della rete in cui sta accedendo.

Iniziamo con uno dei comandi più basilari:

    ipfs id
   
   Con questo comando possiamo ottenere id che ci  è stato assegnato che corrisponde al nostro identificativo all'interno della rete IPFS l'esempio di output potrebbe essere il seguente che ci illustra oltre all'ID anche i vari IPFS-CLUSTER con il quale è in collegamento il nostro IPFS:
	   

    {
        "ID": "12D3KooWCkzQL1mNcn1nugUA8k88mygR2EpdRtEoDyBE3Uncinkz",
        "PublicKey": "CAESICu1tSt5tZsdSW7NM+/A/D46ZVXFPscIsLUs7q/GR07D",
        "Addresses": [
                "/ip4/127.0.0.1/tcp/4001/p2p/12D3KooWCkzQL1mNcn1nugUA8k88mygR2EpdRtEoDyBE3Uncinkz",
                "/ip4/127.0.0.1/udp/4001/quic-v1/p2p/12D3KooWCkzQL1mNcn1nugUA8k88mygR2EpdRtEoDyBE3Uncinkz",
                "/ip4/127.0.0.1/udp/4001/quic-v1/webtransport/certhash/uEiBPWxa6bj8eEC260Fre-spU-kPKaVrn8LNvpcxpEDKYcw/certhash/uEiDA3XQHtyxKbmxYlujbggdb63JjyR5d20AEx-I3C9Nl9A/p2p/12D3KooWCkzQL1mNcn1nugUA8k88mygR2EpdRtEoDyBE3Uncinkz",
                "/ip4/127.0.0.1/udp/4001/quic/p2p/12D3KooWCkzQL1mNcn1nugUA8k88mygR2EpdRtEoDyBE3Uncinkz",
                "/ip4/172.19.0.3/tcp/4001/p2p/12D3KooWCkzQL1mNcn1nugUA8k88mygR2EpdRtEoDyBE3Uncinkz",
                "/ip4/172.19.0.3/udp/4001/quic-v1/p2p/12D3KooWCkzQL1mNcn1nugUA8k88mygR2EpdRtEoDyBE3Uncinkz",
                "/ip4/172.19.0.3/udp/4001/quic-v1/webtransport/certhash/uEiBPWxa6bj8eEC260Fre-spU-kPKaVrn8LNvpcxpEDKYcw/certhash/uEiDA3XQHtyxKbmxYlujbggdb63JjyR5d20AEx-I3C9Nl9A/p2p/12D3KooWCkzQL1mNcn1nugUA8k88mygR2EpdRtEoDyBE3Uncinkz",
                "/ip4/172.19.0.3/udp/4001/quic/p2p/12D3KooWCkzQL1mNcn1nugUA8k88mygR2EpdRtEoDyBE3Uncinkz",
                "/ip4/212.227.227.111/tcp/20112/p2p/12D3KooWCkzQL1mNcn1nugUA8k88mygR2EpdRtEoDyBE3Uncinkz",
                "/ip4/212.227.227.111/udp/8672/quic-v1/p2p/12D3KooWCkzQL1mNcn1nugUA8k88mygR2EpdRtEoDyBE3Uncinkz",
                "/ip4/212.227.227.111/udp/8672/quic-v1/webtransport/certhash/uEiBPWxa6bj8eEC260Fre-spU-kPKaVrn8LNvpcxpEDKYcw/certhash/uEiDA3XQHtyxKbmxYlujbggdb63JjyR5d20AEx-I3C9Nl9A/p2p/12D3KooWCkzQL1mNcn1nugUA8k88mygR2EpdRtEoDyBE3Uncinkz",
                "/ip4/212.227.227.111/udp/8672/quic/p2p/12D3KooWCkzQL1mNcn1nugUA8k88mygR2EpdRtEoDyBE3Uncinkz"
        ],
        "AgentVersion": "kubo/0.20.0/b8c4725/docker",
        "ProtocolVersion": "ipfs/0.1.0",
        "Protocols": [
                "/ipfs/bitswap",
                "/ipfs/bitswap/1.0.0",
                "/ipfs/bitswap/1.1.0",
                "/ipfs/bitswap/1.2.0",
                "/ipfs/id/1.0.0",
                "/ipfs/id/push/1.0.0",
                "/ipfs/kad/1.0.0",
                "/ipfs/lan/kad/1.0.0",
                "/ipfs/ping/1.0.0",
                "/libp2p/autonat/1.0.0",
                "/libp2p/circuit/relay/0.2.0/hop",
                "/libp2p/circuit/relay/0.2.0/stop",
                "/libp2p/dcutr",
                "/x/"
        ]
}

IPFS è la macchina che ha la possibilità di caricare dei file:
	
    # ipfs add name.txt
    
   Viene restituito un hash del file come il seguente
   

    added QmPet72Ep6XFBHqCVrRnSZ77nvcbNEtC2wiBWhHsmki66q try.txt  
    7.82 KiB / 7.82 KiB [========================================================] 100.00%
Con il codice hash è possibile recuperare il file su qualsiasi ipfs client della rete digitando i comandi

   Con il seguente comando viene scaricato il file nel ipfs client locale 

    ipfs get QmPet72Ep6XFBHqCVrRnSZ77nvcbNEtC2wiBWhHsmki66q
    
Con il seguente comando viene stampato il contenuto direttamente in console
  

    ipfs cat QmPet72Ep6XFBHqCVrRnSZ77nvcbNEtC2wiBWhHsmki66q

IPFS a questo punto contiene il file in locale ma non ancora distribuito per effettuare la distribuzione di un file tramite i vari IPFS-CLUSTER che comunicano tra loro è possibile fare questo passaggio lanciando il comando seguente:

    ipfs pin add QmPet72Ep6XFBHqCVrRnSZ77nvcbNEtC2wiBWhHsmki66q

In questo momento il file verra pinnato il file solo nel ipfs locale.
Procediamo con un comando utile che ci permette di trasferire un file caricato da riga di comando all'interno del file system il comando è il seguente:

    ipfs files cp /ipfs/QmPet72Ep6XFBHqCVrRnSZ77nvcbNEtC2wiBWhHsmki66q /try.txt
    
  Dando questo comando se aprissimo l'interfaccia web vedremmo il file al suo interno chiaramente possiamo chiamare il file in locale come preferiamo
 
Ora è possibile scegliere di fare 2 azione pinnare sul IPFS-CLUSTER locale con il seguente comando

    ipfs pin remote add --service cluster0 /ipfs/QmPet72Ep6XFBHqCVrRnSZ77nvcbNEtC2wiBWhHsmki66q

Con questo comando abbiamo avviato il vero processo di distribuzione del file infatti da questo momento sarà possibile trovare il file pinnato all'interno della rete dei cluster possiamo verificare che il file si sta distribuendo all'interno della rete vedendo sui vari ipfs-cluster il seguente comando

    ipfs-cluster-ctl pin ls
    ipfs pin ls --type=all
   
 Infatti verrà ritornata la lista dei vari file che IPFS-CLUSTER ha e sta mantenendo vivi all'interno della rete questo passaggio è fondamentale perchè permetterà di riprendere il file anche se IPFS originale dovesse cadere solo da questo momento sarebbe possibile recuperabile il file.
 

    QmUNCGtFmnwfuTVbcK4ehJ2XkMCH2L6aqY2gsGcFjjDPgg recursive
    QmUNLLsPACCz1vLxQVkXqqLX5R1X345qqfHbsf67hvA3Nn recursive

Per aumentare la diffusione dei file su diversi IPFS-CLUSTER è possibile usufruire di servizi predisposti come Pinata che è possibile configurare e usare con i seguenti comandi
	
    ipfs pin remote service add  Pinata  [https://api.pinata.cloud/psa](https://api.pinata.cloud/psa) <MySecretAPIToken>
    ipfs pin remote ls --service Pinata
La risposta a tale comando dovrebbere essere simile alla seguente

    QmZoEqoxH8WJBreVWJatM8jku7mAzJccAHoULsqkMfycEr pinned  foo_goose.txt

Per rimovere i file non pinnati dal IPFS locale, il comando è il seguente

    ipfs repo gc
il risultato sarà simile al seguente

    > removed QmVoSaWpZYicoLSAcdwxDPt2Gk4WVFCfBFTBtwwY2ASD9P
    > removed QmcpK3cSDyPGiNriMZrZTNu8YCPBSiMAApuvMqXaJVyuWr
    > removed QmdpczDhBmrkxerCUWkEcRExcTHFcA4EcDCeYNdXcV5iqE


Ora vediamo un altro comando che ci permette di visualizza quali utenti hanno il nostro file distribuito, sempre solo usufruendo dell'hash che ha il file in analisi

    ipfs  dht  findprovs  QmazbzGeDqQEfekw1uAN4AhLVjuH4Vg1hjmTVfkQpcJiBe
La risposta sarà un elendo di macchine utente

    12D3KooWT1KuUSdfZYNXzJBMZDHsxyKB4g14z4SYt5ZHZNiYpJRm
    12D3KooWCoxN62pFGidpXwDLY7Q95qoQsVezV6DX3D4byqtsRMg3
l'ultimo comando che potrebbe tornarci comodo sarebbe il link condivisibile per recuperare il file.

    ipfs  swarm  peers  | grep "12D3KooWCoxN62pFGidpXwDLY7Q95qoQsVezV6DX3D4byqtsRMg3"
    
Il risulto è il seguente

    /ip4/172.18.0.3/tcp/4001/p2p/12D3KooWCoxN62pFGidpXwDLY7Q95qoQsVezV6DX3D4byqtsRMg3




