% Last updated: 31-Dec-2011
% Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
% Source: https://github.com/udy11, https://gitlab.com/udy11
% Program to get a 3D profile of intensity of an image

% Intensity is taken as sum of RGB values, so intensity varies: 0-765
% In the 3D plot, the transparency of edges is set to 10%
% Xlsx file will be of the same name as the image file and will be
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