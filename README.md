<h1>Automated Spotify Playlist Creator</h1>
<h2>Overview</h2>
<p>This Program creates a playlist of top 100 songs as per <a href='https://www.billboard.com/charts/hot-100/'> Billboard </a> inside Spotify based on the date passed by the user.</p>
<h2>Program Flow</h2>
<ol>
  <li>Loads the Environment Variables from the .env file.</li>
  <li>Fetches the date from the user validating it.</li>
  <li>Fetches the title of top 100 songs from the billboard website.
    <ul>
      <li>Sends the connection request to the billboard website appending the date in the URL.</li>
      <li>Gets the response from the website.</li>
      <li>Fetches the .html file from the response and stores it inside a variable in Python.</li>
      <li>Scrapes the HTML code for the specific song titles and stores element containing the song titles inside a list.</li>
    </ul>
  </li>
  <li>Intantiates the SpotifyOAuth Object passing the appropriate parameters.</li>
  <li>Authorizes the Third Party App (The Python Code) to access the Spotify Account and sends back the access token as a response (Stored in another .txt file).</li>
  <li>Creates a new Spotify Playlist passing the appropriate parameters.</li>
  <li>Fetches the title of the song from the HTML elements.</li>
  <li>Searches the songs in spotify based on 'Song Title' and the 'Year'.</li>
  <li>Append the song URI in a list from the .json response as a result of the search query via API.</li>
  <ul><li>If song not found, displays appropriate message instead of runtime exception.</li></ul>
  <li>Adds the entire list of found songs inside the playlist created earlier.</li>
</ol>

<h2>Prerequisites</h2>
  <h3>How OAuth works?</h3>
    <p>Spotify uses OAuth to give the Third Party applications access to your account. <br />
    In a nutshell, the access takes place in the form of tokens instead of sharing the actual account credentials. <br />
    Highly recommeded to check out this article. <br />
    <a href="https://developer.okta.com/blog/2017/06/21/what-the-heck-is-oauth">How OAuth works?</a></p>

  <h3>Setting up the Spotify App</h3>
    <ol>
      <li>Sign in or Create an Account with the Spotify
      <ul>
        <li>Verify your email address.</li>
      </ul>
      </li>
      <li>Go to Spotify <a href="https://developer.spotify.com/dashboard">Developer</a> Dashboard and click on 'Create App'.
      <img width="947" alt="image" src="https://github.com/Clandoor/Automated-Spotify-Playlist/assets/42005547/933539ff-b89b-42fd-aa36-912a0a7a2df9">
      </li>
      <li>Enter the appropriate fields. Make sure to set up the 'Redirect URI' to any <strong>valid</strong> URL.
        <ul>
          <li>For example: www.example.com</li>
        </ul>
      </li>
      <li>Once your App is successfully been created, navigate your way inside the App.</li>
      <li>Once inside, click on 'Settings'.
      <img width="952" alt="image" src="https://github.com/Clandoor/Automated-Spotify-Playlist/assets/42005547/797633bb-2957-433f-a6a0-028e6fe57900">
      </li>
      <li>Copy both 'Client ID' and 'Client Secrect'.
        <ul>
          <li>They will be useful to make the first authorization request (From the third party app - Your Python Script) to the Spotify App which you just created.</li>
        </ul>
      <img width="944" alt="image" src="https://github.com/Clandoor/Automated-Spotify-Playlist/assets/42005547/3935a1bd-a0da-43e9-ba86-c7aad8555431">
      </li>
      <li>Make sure to also save the 'Redirect URI'.</li>
      <li>Go to your Spotify Account details and copy your spotify username.
      <img width="917" alt="image" src="https://github.com/Clandoor/Automated-Spotify-Playlist/assets/42005547/ef508ec9-cada-442a-8c2f-32cdcdeceee3">
      </li>
    </ol>
  
  <h3>Storing Sensitive Data as Environment Variables inside PyCharm</h3>
  <p>This part will involve storing all the sensitive data we just got from the previous step as environment variables inside PyCharm.</p>
    <ol>
      <li>Download and Install packages 'dotenv' libraray.</li>
      <li>Store the sensitive data inside the .env file separately inside the <strong>same directory.</strong>
      <img width="448" alt="image" src="https://github.com/Clandoor/Automated-Spotify-Playlist/assets/42005547/e72b2629-eb16-4745-8ff4-f8dcd8440b7f">
      </li>
      <li>Import the OS module and load the environment variables storing them in the actual python variables.
        <img width="436" alt="image" src="https://github.com/Clandoor/Automated-Spotify-Playlist/assets/42005547/dbe2fb8c-8089-470b-9485-74b170cf02f8">
      </li>        
    </ol>

  <h3>Authorizing the Python Script to Access Your Spotify</h3>
  <p>When the code is ran for the first time, it will request the Spotify App for the authorization.</p>
  <p>The Spotify App will send a unique token as a form of authorization instead of directly providing the spotify credentials to the python script.</p>
  <p>When the authorization is successful (Python Script is authorized to access the Spotify App), one will be redirected to the new URL.</p>
  <p>Click on 'Agree' button.</p>
  <img width="263" alt="image" src="https://github.com/Clandoor/Automated-Spotify-Playlist/assets/42005547/acbb3b7b-25c5-4e99-87f0-f555675fe095">
  <p>Simply copy the redirectired URL and paste it in the Python Console.</p>
  <img width="586" alt="image" src="https://github.com/Clandoor/Automated-Spotify-Playlist/assets/42005547/9a4d3e8a-c767-4484-9450-171f0125a858">
    <img width="554" alt="image" src="https://github.com/Clandoor/Automated-Spotify-Playlist/assets/42005547/15362015-0407-4e92-a181-8bbd76141d62">
  <p>As a result, 'token.txt' file will be generated with authorization details which will be used everytime the Python Script tries to access the Spotify App.</p>
  <img width="119" alt="image" src="https://github.com/Clandoor/Automated-Spotify-Playlist/assets/42005547/e8de0ae3-dc10-43c4-9742-497cea55b49a">
  
<h2>Understanding SpotifyOAuth Parameters</h2>
<ol>
  <li>'scope': This parameter will determine what the third party app (Our Python Script) can access in the Spotify App.
  <ul>
    <li>Here, we have set it to 'playlist-modify-private' as per the needs of this project (Can view and edit Private Playlists)</li>
  </ul>
  </li>
  <li>'redirect_uri': Once the authorization is done, the app will be redirected to some URI. Progressing further from that URI, token will be sent to the third party app as a form of authorization.</li>
  <li>'client_id': The ID of the Spotify APP client. Similar to Username.</li>
  <li>'client_secret': Similar to the password. With these two, the third party app can access the Spotify App asking for authorization.</li>
  <li>'cache_path': The name of the file where the token access token will be stored which will be needed to access the Spotify App by the third party client.</li>
  <li>'username': Your Spotify Username.</li>
</ol>
</ol>

<h2>Conclusion</h2>
  <p>Once all these prerequisities are completed, you are good to go.</p>
  <p>Feel free to reach out to me if you run into any issues :)</p>
