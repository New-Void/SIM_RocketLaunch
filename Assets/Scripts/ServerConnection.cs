using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using UnityEditor;

public class ServerConnection : MonoBehaviour
{
    private int trickVarServer;

    private Socket clientServer;
    // Start is called before the first frame update
    void Start()
    {
        StartServer();
        
    }

    void StartServer()
    {
        String[] args = System.Environment.GetCommandLineArgs();
        if (args.Length == 2)
        {
            trickVarServer = int.Parse(args[1]);
        }
        else
        {
            Console.WriteLine("Cannot find port number");
            Application.Quit();
        }

        IPHostEntry ipHost = Dns.GetHostEntry("localhost");
        IPAddress ipAddress = ipHost.AddressList[0];
        IPEndPoint localEndPoint = new IPEndPoint(ipAddress, trickVarServer);
        try
        {
            clientServer = new Socket(ipAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp);

            clientServer.Connect(localEndPoint);

            Console.WriteLine("Socket connected to " + clientServer.RemoteEndPoint.ToString());
                
            clientServer.Send(Encoding.ASCII.GetBytes("trick.var_pause()\n"));
            clientServer.Send(Encoding.ASCII.GetBytes("trick.var_ascii()\n"));
            clientServer.Send(Encoding.ASCII.GetBytes("trick.var_add(\"dyn.rocket.pos[0]\") \n " + 
                                                             "trick.var_add(\"dyn.rocket.pos[1]\") \n"));

            clientServer.Send(Encoding.ASCII.GetBytes("trick.var_unpause()\n"));
            
            //Receiving Messages from server
            RecieveData();
            
        }
        catch (Exception e)
        {
            Console.WriteLine(e);
            throw;
        }
    }

    private void RecieveData()
    {
        while (true)
        {
            byte[] buffer = new byte[1024];

            var bytesRead = clientServer.Receive(buffer);

            String dataRead = Encoding.ASCII.GetString(buffer,0, bytesRead );

            String[] data = dataRead.Split("\t");

            GameManager.Instance.rocketX = float.Parse(data[1]);
            GameManager.Instance.rocketY = float.Parse(data[1]);

        }
    }

    private void Update()
    {
        
    }
}
