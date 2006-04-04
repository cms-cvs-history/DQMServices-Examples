#ifndef _DQMServices_Examples_ClientWithWebInterface_h_
#define _DQMServices_Examples_ClientWithWebInterface_h_

#include "DQMServices/Components/interface/DQMBaseClient.h"
#include "DQMServices/Components/interface/Updater.h"
#include "DQMServices/Components/interface/UpdateObserver.h"

#include "DQMServices/Core/interface/MonitorUserInterface.h"

#include "DQMServices/Examples/interface/ExampleWebInterface.h"

#include <vector>
#include <string>
#include <iostream>

class ClientWithWebInterface : public DQMBaseClient, 
		      public dqm::UpdateObserver
{
public:
  
  XDAQ_INSTANTIATOR();
  
  ClientWithWebInterface(xdaq::ApplicationStub *s);

  // implement the method that outputs the page with the widgets (declared in DQMBaseClient):
  void general(xgi::Input * in, xgi::Output * out ) throw (xgi::exception::Exception);

  // the method which answers all HTTP requests of the form ".../Request?RequestID=..."
  void handleWebRequest(xgi::Input * in, xgi::Output * out);

  // this obligatory method is called whenever the client enters the "Configured" state:
  void configure();

  // this obligatory method is called whenever the client enters the "Enabled" state:
  void newRun();

  // this obligatory method is called whenever the client enters the "Halted" state:
  void endRun();

  // this obligatory method is called by the Updater component, whenever there is an update 
  void onUpdate() const;


public:
  
  ExampleWebInterface * webInterface_p;
};

XDAQ_INSTANTIATOR_IMPL(ClientWithWebInterface)

#endif
