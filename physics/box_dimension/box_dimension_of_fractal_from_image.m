% Last updated: 09-Jul-2012
% Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
% Source: https://github.com/udy11, https://gitlab.com/udy11
% Program to find Box Dimension (or Fractal Dimension) from
% a Black-&-White image

% The program calculates the number of boxes of different sizes 
% (as per input bs) required to cover the image. It uses fixed boxes
% (instead of sliding boxes, which I think is better but rather
% code-wise challenging) to see how many boxes cover the image.

% After calculating number of boxes required (say, n) to cover the
% image with respect to sizes (say, s), the slope of plot
% of log(n) vs. -log(s) gives the dimension
% Method of least squares is used to calculate it.
% Variable cc has first column log(n) and second -log(s).
% Variable slp is slope and int is intercept of the fitted line.
% Later program shows the plot as well as fitted line.
% The fitted line is black dash-dash line in the plot.

% The program will work correctly as long as
% the background is black (i.e. #000000). A color inverter is
% given as an option in case background is white (i.e. #FFFFFF).
% In case of something else please use the program
% "program_to_convert_image_to_black-&-white_based_on_RGB_values"
% to choose background and foreground as per your choice.

% {{{ Add error calculations }}}

imfl=input('Enter the input filename with extension in single quotes: ');
img=imread(imfl);
sz=size(img);
invc=input('Enter 1 to interchange black and white: ');
if invc==1
    img(:,:,:)=abs(255-img(:,:,:));
end
bs=input('Enter the box size range in pixels as [min step max]: ');
while(bs(1)<1 || bs(3)>min(sz(1),sz(2)) || bs(3)<bs(1))
    bs=input('Please enter box size range correctly: ');
end
cc=zeros(bs(3),2);
for i=bs(1):bs(2):bs(3)
    cc(i,1)=i;
    for jr=1:floor(sz(1)/i)
        for jc=1:floor(sz(2)/i)
            if(sum(sum(img(1+(jr-1)*i:jr*i,1+(jc-1)*i:jc*i,1),2))>0)
                cc(i,2)=cc(i,2)+1;
            end
        end
        if(sum(sum(img(1+(jr-1)*i:jr*i,i*floor(sz(2)/i)+1:sz(2),1)))>0)
            cc(i,2)=cc(i,2)+1;
        end
    end
    for jc=1:floor(sz(2)/i)
        if(sum(sum(img(i*floor(sz(1)/i)+1:sz(1),1+(jc-1)*i:jc*i,1)))>0)
            cc(i,2)=cc(i,2)+1;
        end
    end
    if(sum(sum(img(i*floor(sz(1)/i)+1:sz(1),i*floor(sz(2)/i)+1:sz(2),1)))>0)
      	cc(i,2)=cc(i,2)+1;
    end
end
cc(bs(1):bs(2):bs(3),2)=log(cc(bs(1):bs(2):bs(3),2));
cc(bs(1):bs(2):bs(3),1)=-log(cc(bs(1):bs(2):bs(3),1));
plot(cc(bs(1):bs(2):bs(3),1),cc(bs(1):bs(2):bs(3),2));
xlabel('-log(Box Size)');
ylabel('log(Number of Boxes)');
hold on
sx=sum(cc(bs(1):bs(2):bs(3),1));
sy=sum(cc(bs(1):bs(2):bs(3),2));
sx2=0; sxy=0;
for i=bs(1):bs(2):bs(3)
    sx2=sx2+cc(i,1)*cc(i,1);
    sxy=sxy+cc(i,1)*cc(i,2);
end
nn=floor((bs(3)-bs(1))/bs(2))+1;
slp=(sxy-sx*sy/nn)/(sx2-sx*sx/nn);
fprintf('Box Dimension is: %d\n',slp);
int=sy/nn-slp*sx/nn;
plot(cc(bs(1):bs(2):bs(3),1),cc(bs(1):bs(2):bs(3),1)*slp+int,'--k');
hold off
clear sx sy sx2 sxy nn bs imfl img bs i invc jc jr sz
