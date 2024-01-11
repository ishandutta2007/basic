% Last updated: 31-Dec-2011
% Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
% Source: https://github.com/udy11, https://gitlab.com/udy11
% Program to get a 3D profile of intensity of an image and do some further analysis

% Program to get a 3D profile of intensity of an image
% Intensity is taken as sum of RGB values, so intensity varies: 0-765
% In the 3D plot, the transparency of edges is set to 10%
% Xls file will be of the same name as the image file and will be
% overwritten if already exists

disp('Make the following entries in single quotes.');
f1n=input('Enter image file name: ' );
f2n=input('Enter file extension: ' );
f2n=[f1n,'.',f2n];
im9=double(imread(f2n));
im9d=im9(:,:,1)+im9(:,:,2)+im9(:,:,3);
surf(im9d,'EdgeAlpha',0.1)
ch0s=input('Press 1 to overwrite intensity to the Excel file (of same name)');
if ch0s==1
    xlswrite([f1n,'.','xlsx'],im9d);
end

% For further analysis, user is asked to indicate central maxima's position
% on the image to get an intensity line segment of the image. On this
% segment then the user is asked to indicate further maxima's positions

imshow(f2n);title('Select the Central Maxima');
cxy(1:2)=ginput(1);
ch1s=input('Press 1 for up, increasing clockwise: ');
if ch1s==1
    infxy=im9d(floor(cxy(1)),floor(cxy(2)):-1:1);
end
plot(infxy(1,:));
nmi1=0;
nmx=input('Enter the number of maxima to select: ');
mxm=zeros(nmx,2);
for j=1:nmx
    title(['Select point #',j+48]);
    mxm(j,:)=ginput(1);
end