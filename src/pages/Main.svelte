<script>
  import { onMount } from "svelte";
  import Footer from "../components/Footer.svelte";
  import { getDatabase, ref, onValue } from "firebase/database";

  let hour = new Date().getHours().toString().padStart(2, "0");
  let min = new Date().getMinutes().toString().padStart(2, "0");

  $: items = [];

  const db = getDatabase();
  const itemsRef = ref(db, "/items/");
  onMount(() => {
    onValue(itemsRef, (snapshot) => {
      const data = snapshot.val();
      items = Object.values(data).reverse();
    });
  });

  const calcTime = (timestamp) => {
    // new Date().getTime()은 항상 UTC 기준이므로, 별도 시간 보정이 불필요합니다.
    const diff = new Date().getTime() - timestamp;

    const seconds = Math.floor(diff / 1000);
    const minutes = Math.floor(seconds / 60);
    const hours = Math.floor(minutes / 60);
    const days = Math.floor(hours / 24);

    if (days > 0) return `${days}일 전`;
    if (hours > 0) return `${hours}시간 전`;
    if (minutes > 0) return `${minutes}분 전`;
    if (seconds > 0) return `${seconds}초 전`;
    return "방금 전";
  };
</script>

<header>
  <div class="info-bar">
    <div class="info-bar__time">{hour}:{min}</div>
    <div class="info-bar__icons">
      <img src="assets/chart-bar.svg" alt="chart-bar" />
      <img src="assets/wifi.svg" alt="wifi" />
      <img src="assets/battery.svg" alt="battery" />
    </div>
  </div>
  <div class="menu-bar">
    <div class="menu-bar__location">
      <div>역삼1동</div>
      <div class="menu-bar__location-icon">
        <img src="assets/arrow.svg" alt="arrow" />
      </div>
    </div>
    <div class="menu-bar__icons">
      <img src="assets/search.svg" alt="search" />
      <img src="assets/menu.svg" alt="menu" />
      <img src="assets/alert.svg" alt="alert" />
    </div>
  </div>
</header>
<!-- 헤더 부분 끝 -->

<!-- 메인 부분 시작 -->
<main>
  {#each items as item}
    <div class="item-list">
      <div class="item-list__img">
        <img src={item.imgUrl} alt={item.title} />
      </div>
      <div class="item-list__info">
        <div class="item-list__info-title">{item.title}</div>
        <div class="item-list__info-price">
          {item.price}
        </div>
        <div class="item-list__info-description">{item.description}</div>
        <div class="item-list__info-meta">
          {item.place}
          {calcTime(item.insertAt)}
        </div>
      </div>
    </div>
  {/each}
  <a class="write-btn" href="#/Write">+ 글쓰기</a>
</main>

<Footer location="home" />

<!-- 메인 부분 끝 -->

<!-- 푸터 부분 시작 -->

<style>
  .info-bar__time {
    color: blue;
  }
</style>
