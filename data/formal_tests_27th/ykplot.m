function ykplot

[h0,m0] = csvreadh('fft_gs_mar24_800us_unloaded_0.csv', ',');
[h1,m1] = csvreadh('fft_gs_mar24_800us_unloaded_1.csv', ',');
[h2,m2] = csvreadh('fft_gs_mar24_800us_unloaded_2.csv', ',');
[h3,m3] = csvreadh('fft_gs_mar24_800us_unloaded_3.csv', ',');
[h4,m4] = csvreadh('fft_gs_mar24_800us_unloaded_4.csv', ',');
[h5,m5] = csvreadh('fft_gs_mar24_800us_unloaded_5.csv', ',');
[h6,m6] = csvreadh('fft_gs_mar24_800us_unloaded_6.csv', ',');
[h7,m7] = csvreadh('fft_gs_mar24_800us_unloaded_7.csv', ',');
[h8,m8] = csvreadh('fft_gs_mar24_800us_unloaded_8.csv', ',');
[h9,m9] = csvreadh('fft_gs_mar24_800us_unloaded_9.csv', ',');

f = m0(1:500,1);
M_all = (m0+m1+m2+m3+m4+m5+m6+m7+m8+m9)/10;
X = M_all(1:500,2);
Y = M_all(1:500,3);
Z = M_all(1:500,4);

figure
subplot(3,1,1)
plot(f,X)
title('X')
subplot(3,1,2)
title('Y')
plot(f,Y)
subplot(3,1,3)
title('Z')
plot(f,Z)

return