using UnityEngine;
using System.Collections;
using UnityEngine.Networking;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;

public class Server : MonoBehaviour
{
public GameObject m_text;

public int hostId;
public int myReiliableChannelId;

// Use this for initialization
void Start()
{
Application.runInBackground = true;
try {
//listen on: 127.0.0.1:8008
// Network.InitializeSecurity();
//NetworkServer.Listen(8008);
//NetworkServer.RegisterHandler(MsgType.Connect, OnConnect);
NetworkTransport.Init();

ConnectionConfig config = new ConnectionConfig();
myReiliableChannelId = config.AddChannel(QosType.Reliable);
//int myUnreliableChannelId = config.AddChannel(QosType.Unreliable);

HostTopology topology = new HostTopology(config, 10);

hostId = NetworkTransport.AddHost(topology, 8008);

Debug.Log("started server");
} catch
{
Debug.Log("unable to start server");
}
}

public void OnConnect(NetworkMessage netMsg)
{
Debug.Log(netMsg);
}

// Update is called once per frame
void Update()
{
int recHostId;
int connectionId;
int channelId;
byte[] recBuffer = new byte[1024];
int bufferSize = 1024;
int dataSize;
byte error;
NetworkEventType recData = NetworkTransport.Receive(out recHostId, out connectionId, out channelId, recBuffer, bufferSize, out dataSize, out error);



if (dataSize > 0)
{
m_text.GetComponent<TextMesh>().text = recBuffer.ToString();
Debug.Log("error: " + error.ToString());
Debug.Log("Data size was: " + dataSize.ToString());
Debug.Log("recBuffer: " + recBuffer.ToString());
}

switch (recData)
{
case NetworkEventType.Nothing: //1
break;
case NetworkEventType.ConnectEvent: //2
Debug.Log("incoming connection event received");
break;
case NetworkEventType.DataEvent: //3
Stream stream = new MemoryStream(recBuffer);
BinaryFormatter formatter = new BinaryFormatter();
string message = formatter.Deserialize(stream) as string;
Debug.Log("incoming message event received: " + message);
break;
case NetworkEventType.DisconnectEvent: //4
Debug.Log("remote client event disconnected");
break;
}
}

void OnGUI()
{
if (GUI.Button(new Rect(10, 70, 50, 30), "Click"))
{
byte error;
int connectionId = NetworkTransport.Connect(hostId, "127.0.0.1", 8008, 0, out error);
Debug.Log("Connected to server. ConnectionId: " + connectionId);

byte[] buffer = new byte[1024];
Stream stream = new MemoryStream(buffer);
BinaryFormatter formatter = new BinaryFormatter();
formatter.Serialize(stream, "HelloServer");

int bufferSize = 1024;

NetworkTransport.Sed(hostId, connectionId, myReiliableChannelId, buffer, bufferSize, out error);
}
}
}
