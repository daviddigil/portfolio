// Case study pages: nav state, scroll reveal, section dividers, cursor sparks.
// Lighter than the homepage's full threads/portrait/GSAP stack — these are reading pages.
(function(){
  const nav=document.querySelector('nav');
  if(nav)nav.classList.add('solid');

  // scroll reveal — rootMargin triggers as soon as an element's top edge nears the viewport,
  // regardless of the element's own height (a tall .cs-body never needs to be mostly on-screen).
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:0,rootMargin:'0px 0px -10% 0px'});
  document.querySelectorAll('.rv').forEach((el,i)=>{el.style.transitionDelay=(i%4)*70+'ms';io.observe(el)});

  // section dividers: thin thread draws left-to-right on scroll-in
  const dio=new IntersectionObserver(es=>es.forEach(e=>{
    const d=e.target.querySelector(':scope>.divider');
    if(e.isIntersecting&&d){d.classList.add('on');dio.unobserve(e.target)}
  }),{threshold:.05});
  document.querySelectorAll('section').forEach(s=>{
    const d=document.createElement('i');d.className='divider';s.insertBefore(d,s.firstChild);dio.observe(s);
  });

  if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;

  // cursor sparks (desktop only) — same visual language as the homepage
  if(matchMedia('(hover:hover) and (pointer:fine)').matches){
    const cv=document.createElement('canvas');cv.id='fx';cv.setAttribute('aria-hidden','true');document.body.appendChild(cv);
    const cx=cv.getContext('2d');let W=0,H=0,dpr=1,raf=0;
    const rs=()=>{dpr=Math.min(2,devicePixelRatio||1);W=innerWidth;H=innerHeight;cv.width=W*dpr;cv.height=H*dpr};rs();addEventListener('resize',rs);
    const P=[],cur={x:0,y:0,tx:0,ty:0,on:false,lx:0,ly:0};let idleAt=0,prev=0;
    function loop(ts){
      raf=0;const dt=Math.min(.05,(ts-prev)/1000)||.016,f=dt*60;prev=ts;
      cx.setTransform(dpr,0,0,dpr,0,0);cx.clearRect(0,0,W,H);cx.globalCompositeOperation='lighter';
      for(let i=P.length-1;i>=0;i--){
        const p=P[i];p.l+=dt;if(p.l>=p.m){P.splice(i,1);continue}
        p.x+=p.vx*f;p.y+=p.vy*f;p.vx*=.96;p.vy*=.96;const a=1-p.l/p.m;
        cx.fillStyle='rgba('+p.c+','+a+')';cx.beginPath();cx.arc(p.x,p.y,p.r,0,6.283);cx.fill();
      }
      if(cur.on){
        cur.x+=(cur.tx-cur.x)*.4;cur.y+=(cur.ty-cur.y)*.4;
        const g=cx.createRadialGradient(cur.x,cur.y,0,cur.x,cur.y,16);g.addColorStop(0,'rgba(127,233,255,.45)');g.addColorStop(1,'rgba(127,233,255,0)');
        cx.fillStyle=g;cx.fillRect(cur.x-16,cur.y-16,32,32);cx.fillStyle='#E6FDFF';cx.beginPath();cx.arc(cur.x,cur.y,2.2,0,6.283);cx.fill();
      }
      if(P.length||performance.now()<idleAt)raf=requestAnimationFrame(loop);
    }
    function kick(){if(!raf&&!document.hidden){prev=performance.now();raf=requestAnimationFrame(loop)}}
    addEventListener('pointermove',e=>{
      if(e.pointerType==='touch')return;
      if(!cur.on){cur.x=e.clientX;cur.y=e.clientY}
      cur.on=true;cur.tx=e.clientX;cur.ty=e.clientY;idleAt=performance.now()+1200;
      if(Math.hypot(e.clientX-cur.lx,e.clientY-cur.ly)>22){
        cur.lx=e.clientX;cur.ly=e.clientY;
        P.push({x:e.clientX,y:e.clientY,vx:(Math.random()-.5)*.6,vy:(Math.random()-.5)*.6,l:0,m:.5+Math.random()*.4,c:'127,233,255',r:.8+Math.random()*1.3});
      }
      kick();
    },{passive:true});
    document.addEventListener('mouseleave',()=>{cur.on=false});
  }
})();
