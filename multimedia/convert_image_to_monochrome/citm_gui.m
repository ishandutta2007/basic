% Last updated: 08-Jul-2012
% Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
% Source: https://github.com/udy11, https://gitlab.com/udy11
% Program (GUI) to convert an image file in monochrome
% (black and white) based on selected RGB values

% The program reads the input image file
% then shows the user the image with RGB
% sliders (values in 0-255).
% These values decide which pixels to
% whiten and which to blacken.
% Then user is asked if an inversion
% between white and black is intended.
% Finally, the output image is asked to save.

% A 1000 X 1000 dimension image file will take >4 seconds
% to process the whole image once you change any RGB slider.
% Hence it will be better if you work with a small sample, preferably
% a cropped version within 300 X 300, then use tcitmbwborgbv_direct.m
% to convert the whole image at once.

function tcitbwborgbv_gui()
img_fl=input('Enter input image filename with extension in single quotes: ');
img=imread(img_fl);
sz=size(img);
if sz(1)*sz(2)>249999
    warning('Large image size encountered. It is recommended that you take a small sample of this file and work with that, then use tcitmbwborgbv_direct.m to process whole image.');
end
img1=img;
for i=1:sz(1)
    for j=1:sz(2)
        if(img1(i,j,:)>100)
            img1(i,j,:)=255;
        else
            img1(i,j,:)=0;
        end
    end
end
fgr=figure();
fgx=axes('Parent',fgr);
sob=uicontrol('Parent',fgr,'Style','slider',...
    'Value',100,'Min',0,'Max',255,'SliderStep',...
    [1 10]./255,'Position',[100 5 400 15],'Callback',@slider_Callback);
uicontrol('Parent',fgr,'Style','text','Position',...
    [50 7 40 12],'String','Blue');
stb=uicontrol('Parent',fgr,'Style','text','Position',...
    [510 7 30 12],'String','100');
sog=uicontrol('Parent',fgr,'Style','slider',...
    'Value',100,'Min',0,'Max',255,'SliderStep',...
    [1 10]./255,'Position',[100 25 400 15],'Callback',@slider_Callback);
uicontrol('Parent',fgr,'Style','text','Position',...
    [50 27 40 12],'String','Green');
stg=uicontrol('Parent',fgr,'Style','text','Position',...
    [510 27 30 12],'String','100');
sor=uicontrol('Parent',fgr,'Style','slider',...
    'Value',100,'Min',0,'Max',255,'SliderStep',...
    [1 10]./255,'Position',[100 45 400 15],'Callback',@slider_Callback);
uicontrol('Parent',fgr,'Style','text','Position',...
    [50 47 40 12],'String','Red');
str=uicontrol('Parent',fgr,'Style','text','Position',...
    [510 47 30 12],'String','100');
imshow(img1,'Parent',fgx);
input('Enter 1 after you have chosen RGB values: ');
rr=round(get(sor,'Value'));
gg=round(get(sog,'Value'));
bb=round(get(sob,'Value'));
close(fgr);
for i=1:sz(1)
    for j=1:sz(2)
        if(img1(i,j,1)>=rr && img1(i,j,2)>=gg && img1(i,j,3)>=bb)
            img1(i,j,:)=255;
        else
            img1(i,j,:)=0;
        end
    end
end
invc=input('Enter 1 if you want to interchange black and white: ');
if invc==1
    img1(:,:,:)=abs(255-img1(:,:,:));
end
svfl=input('Enter the output filename in single quotes: ');
svxt=input('Enter its desired file format in single quotes: ');
imwrite(img1,[svfl '.' svxt],svxt);

function slider_Callback(~,~)
    b=round(get(sob,'Value'));
    g=round(get(sog,'Value'));
    r=round(get(sor,'Value'));
for i=1:sz(1)
    for j=1:sz(2)
        if(img1(i,j,1)>=r && img1(i,j,2)>=g && img1(i,j,3)>=b)
            img1(i,j,:)=255;
        else
            img1(i,j,:)=0;
        end
    end
end
set(str,'String',num2str(r))
set(stg,'String',num2str(g))
set(stb,'String',num2str(b))
imshow(img1,'Parent',fgx);
img1=img;
end

end