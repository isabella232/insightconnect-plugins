package actions

import (
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/fullcontact/connection"
)

// Validate will validate the input is properly setup with whatever rules you put in
// You can also use this to pre-set any values before they are run by the Run method.
// Note that for Actions, the  Input message is inspected every time time, just before it
// is handed to the Run method. Keep this in mind when setting any properties on the Input i
// You can return a set of errors for any reason to fail the step.
// Otherwise, return nil for success
func (i *LookUpByEmailInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)

	// Custom validation code here
	// Append errors as needed

	// return
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate will validate the output is properly setup with whatever rules you put in
// You can leave this blank if you want to, but if you need to enforce restrictions
// here is where you can return a number of errors. Otherwise, return nil for success
func (o *LookUpByEmailOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)

	// Custom validation code here
	// Append errors as needed

	// return
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run will run the action with the given input over the given connection
func (a *LookUpByEmailAction) Run(conn *connection.Connection, input *LookUpByEmailInput, log plog.Logger) (*LookUpByEmailOutput, error) {
	output := LookUpByEmailOutput{}
	// Your code here
	params := implementationParams{
		ServerBase:     conn.Server,
		Service:        "person.json",
		URLKeys:        []string{"email"},
		URLValues:      []string{input.Email},
		ApplicationKey: conn.Token.SecretKey,
		TimeoutInSec:   10,
	}
	marshaledJSON := Query(params)
	shouldRetry := Postprocess(marshaledJSON, Receivers{PersonPtr: &output.PersonInfo}, 10)
	if shouldRetry {
		marshaledJSON := Query(params)
		Postprocess(marshaledJSON, Receivers{PersonPtr: &output.PersonInfo}, 0)
	}

	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return &output, nil
}

// Test will test the action with the given input over the given connection.
// For this, you should design the output result to be used with the tests in the test/ directory.
// You do not need to / should not need to invoke the actual API, this is just for testing.
func (a *LookUpByEmailAction) Test(conn *connection.Connection, input *LookUpByEmailInput, log plog.Logger) (*LookUpByEmailOutput, error) {
	output := &LookUpByEmailOutput{}
	// Your code here
	// NOTE: The input you receive in the test method cannot be gauranteed to contain "good" value.
	// You should not assume the input is something you can trust in this context.

	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return output, nil
}