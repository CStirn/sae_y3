import org.bson.types.ObjectId;

import java.io.*;
import java.net.*;
import java.util.ArrayList;
import java.util.List;

class ThreadServer extends Thread {

	BufferedReader br;
	PrintStream ps;
	Socket sock;
	DataExchanger exchanger;
	int idThread;

	public ThreadServer(int idThread, Socket sock, DataExchanger data) {
		this.sock = sock;
		this.idThread = idThread;
		this.exchanger = data;
	}

	public void run() {

		try {
			br = new BufferedReader(new InputStreamReader(sock.getInputStream()));
			ps = new PrintStream(sock.getOutputStream());
		}
		catch(IOException e) {
			System.err.println("Thread "+ idThread +": cannot create streams. Aborting.");
			return;
		}
		requestLoop();
		System.out.println("end of thread "+ idThread);
	}

	public void requestLoop() {

		String req = "", res = "", idReq;
		String[] reqParts, argsReq;

		try {
			while(true) {
				req = br.readLine();
				if ((req == null) || (req.isEmpty())) {
					break;
				}

				reqParts = req.split(":");  // Split between the request name and the args
				idReq = reqParts[0];
				argsReq = req.split(",");
				for (int i = 0; i < argsReq.length; i++) {
					argsReq[i] = argsReq[i].trim();
				}

				// Recieving measurements from the drone
				if ("DRONE.SendMeasurement".equals(idReq)) {
					res = recieveSensorMeasurement(argsReq);
				}

				else if ("STOREMEASURE".equals(idReq)) {
					// TODO
				}

				else if ("STOREANALYSIS".equals(idReq)) {
					// TODO
				}

				// Invalid request
				else {
					res = "ERR Invalid request name";
				}

				ps.println(res);
			}
			System.out.println("end of request loop");
		}
		catch(IOException e) {
			System.out.println("problem with receiving request: "+e.getMessage());
		}
	}

	protected String recieveSensorMeasurement(String[] args) throws IOException
	{
		// remove the identifier+uc from params
		if (args.length == 0) {
			return "ERR No data provided";
		}

		// Range sensor (left)
		if ("RangeSensorLeft".equals(args[0])) {
			if (args.length != 2) {
				return "ERR Invalid measurement provided";
			}

			try {
				float measurement = Float.parseFloat(args[1]);
				System.out.println("Measurement for 'Range sensor (left)': " + measurement);
			} catch (NumberFormatException e) {
				return "ERR Invalid measurement provided";
			}
		}

		// Invalid/unhandled sensor
		else {
			return "ERR Invalid sensor";
		}

		return "ERR Unknown";
	}
}

		
