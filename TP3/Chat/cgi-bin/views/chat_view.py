def chat_view(nickname): 

    return """
        <div id="sidepanel">
          <div id="profile">
            <div class="wrap">
              <p id="nickName">{}</p>
            </div>
          </div>
          <div id="search">
            <label for="">
              <i class="fa fa-search" aria-hidden="true"></i>
            </label>
            <input type="text" placeholder="Search contacts..." />
          </div>
          <div id="contacts">
            <ul id="users-list">

            </ul>

          </div>

        </div>


        <div class="content">

          <div class="contact-profile">
            <button id="logout" onclick="logout()" class="btn btn-info" type="button">Logout</button>
          </div>


          <div class="messages">
            <ul id="lista-mensajes">

            </ul>
          </div>

          <div class="message-input">
            <div class="wrap">
              <form id="form-msg">
                <div class="form-group">
                  <input type="text" name="message" placeholder="Write your message..." />
                  <i class="fa fa-paperclip attachment" aria-hidden="true"></i>
                  <button id="btn-send" type="submit" onclick="send_message()" >
                    <i class="fa fa-paper-plane" aria-hidden="true"></i>
                  </button>
                </div>
              </form>
            </div>
          </div>

        </div>

    """.format(nickname)