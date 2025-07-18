<script>
  import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";
  import { user$ } from "../store";

  const provider = new GoogleAuthProvider();
  const auth = getAuth();

  const loginWithGoogle = async () => {
    try {
      const result = await signInWithPopup(auth, provider);
      const credential = GoogleAuthProvider.credentialFromResult(result);
      const token = credential.accessToken;
      const user = result.user;
      user$.set(user);
      localStorage.setItem("token", token);
    } catch (error) {
      console.error(error);
    }
  };
</script>

<div>
  <div>로그인하기</div>
  <button class="login-btn" on:click={loginWithGoogle}>
    <img
      class="google-img"
      src="https://img.lovepik.com/png/20231120/google-internet-icon-vector-Google-system-engineer_642910_wh860.png"
      alt=""
    />
    <div>Google로 시작하기</div>
  </button>
</div>

<style>
  .login-btn {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 200px;
    height: 50px;
    border: 1px solid gray;
    cursor: pointer;
    border-radius: 3px;
  }

  .google-img {
    width: 20px;
  }
</style>
