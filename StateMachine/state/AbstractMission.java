public class AbstractMission {
	protected States state;
	// state variables
	protected ASSIStates ASSI;
	protected boolean ts;

	// constructor
	public AbstractMission() {
		state = States.AS_READY;
	}

	// overall run method
	public void run() {
		switch (state) {
			case AS_READY :
				this.runASReady();
				this.run();
				break;

			case AS_DRIVING :
				this.runASDriving();
				break;
		}
	}

	// state specific run method
	protected void runASDriving() {
		System.out.println("abstract driving");
	}

	protected void runASReady() {
		System.out.println("abstract ready");

		this.transition(States.AS_DRIVING);
	}

	protected void transition(States gotoState) {
		switch (state) {
			case AS_READY :
				if (gotoState == States.AS_DRIVING)
					state = States.AS_DRIVING;
				break;

			case AS_DRIVING :
				break;
		}
	}
}

enum ASSIStates {
	FLASHING
}