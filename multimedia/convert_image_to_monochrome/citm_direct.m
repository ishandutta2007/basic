% Last updated: 08-Jul-2012
% Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
% Source: https://github.com/udy11, https://gitlab.com/udy11
% Program (GUI) to convert an image file in monochrome
% (black and white) based on selected RGB values

% The program reads the input image file
% then asks user to enter RGB values (between 0-255)
% above which a pixel will be whitened.
% Then user is asked if an inversion
% between white and black is intended.
% Finally, the output image is asked to save.

% This program is useful if you want to work with large image files
% To know the RGB values for any file use tcitmbwborgbv_gui.m
% If image file is large, take a sample of it to know appropriate
% RGB values using tcitmbwborgbv_gui.m, then use thi program to
% get your final image directly.

function tcitbwborgbv_direct()
img_fl=input('Enter input image filename with extension in single quotes: ');
img=imread(img_fl);
sz=size(img);
rgb=input('Enter RGB values above which pixels will be whitened (Enter as [r g b]): ');
for i=1:sz(1)
    for j=1:sz(2)
        if(img(i,j,1)>=rgb(1) && img(i,j,2)>=rgb(2) && img(i,j,3)>=rgb(3))
            img(i,j,:)=255;
        else
            img(i,j,:)=0;
        end
    end
end
invc=input('Enter 1 if you want to interchange black and white: ');
if invc==1
    img(:,:,:)=abs(255-img(:,:,:));
end
svfl=input('Enter the output filename in single quotes: ');
svxt=input('Enter its desired file format in single quotes: ');
imwrite(img,[svfl '.' svxt],svxt);
end