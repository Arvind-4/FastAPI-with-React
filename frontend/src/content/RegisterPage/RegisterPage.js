import React from 'react';
import { TextInput, Button, Link } from '@carbon/react';

import './_register-page.css';
const RegisterPage = () => {
  return (
    <div class="register-body">
      <div class="container">
        <div class="row">
          <div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
            <div class="card border-0 shadow rounded-3 my-5">
              <div class="card-body p-4 p-sm-5">
                <h5 class="card-title text-center mb-5 fw-light fs-5">
                  Register Here
                </h5>
                <form>
                  <label>Username</label>
                  <div class="my-3">
                    <TextInput
                      type="text"
                      placeholder="Enter Your Username..."
                    />
                  </div>
                  <label>Email address</label>
                  <div class="my-3">
                    <TextInput type="email" placeholder="Enter Your Email..." />
                  </div>
                  <label>Password</label>
                  <div class="my-3">
                    <TextInput
                      type="password"
                      placeholder="Enter Your Password..."
                    />
                  </div>

                  <div class="text-center">
                    <Button
                      className="btn btn-primary btn-login text-uppercase fw-bold"
                      type="submit">
                      Register
                    </Button>
                  </div>
                  <hr class="my-4" />
                  <div class="text-center">
                    <p class="mb-2">Already have an account?</p>
                    <a href="/login">
                      <Button
                        kind="ghost"
                        className="btn btn-primary btn-login text-uppercase fw-bold">
                        Login Here.
                      </Button>
                    </a>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RegisterPage;
