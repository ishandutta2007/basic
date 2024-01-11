% Last updated: 26-May-2012
% Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
% Source: https://github.com/udy11, https://gitlab.com/udy11
% Program to track a point in a video and get its position & velocity

% {{Add tracking-show-option}}
% {{Show Progress and eta, and possibly live plotting}}
% Idea is simple, compare rgb of selected target in (i-1) frame to that in
% (i) frame, set it as the next target's x-y

% Before running this program:
% To convert from any format to an mmreader compatible format, use ffmpeg
% For cropping, re-timing, contrasting, etc., use ImageJ
% To watch video frame-by-frame, use ImageJ

vdeo=input('Enter video file name in single quotes: ');      % asking for video file's name
vddt=mmreader(vdeo);                        % collecting video data
mv=read(vddt);                              % reading video
tnfr=get(vddt,'NumberOfFrames');            % acquiring total frames
dt=tnfr/get(vddt,'Duration');               % getting fps for velocity calculations
fprintf('Total frames: %1.0f\n',tnfr)       % printing total frames
fr_strt=input('Enter frame # to start: ');  % asking frame to begin with
fr_end=input('Enter frame # to end: ');     % asking frame to end at
nbr=input('Enter search neighborhood area around the target in pixels: ');       % asking neighborhood of target to check
rgbde=input('Enter unexpected RGB difference (1-765): ');      % if this total RGB difference is crossed, error is shown
xy=zeros(fr_end,8);                         % pre-allocating resultant matrix
cc=zeros(2*nbr+1,2*nbr+1,3);                % pre-allocating temp-color matrix {{useless, may be useful later}}
img=mv(:,:,:,fr_strt);                      % setting first frame to get the target
vsz=size(img); vh=vsz(1); vw=vsz(2);        % acquiring video dimensions
imshow(img),title('Select the target');     % showing first selected frame
xy(fr_strt,2:3)=round(ginput(1));                  % asking to select the target
xy(fr_strt,6:8)=img(xy(fr_strt,3),xy(fr_strt,2),:);        % acquiring rgb of target
xy(fr_strt,1)=fr_strt/dt;                   % settting xy(fr_strt,1) as time of first frame
i=fr_strt+1;                                % initialization for main while-loop
while i<fr_end+1                            % beginning main while-loop, i represents frame #
    c0=xy(i-1,6:8);                         % setting c0 as target's rgb in (i-1) frame
    min=765;                                % setting min for comparison, {{think something better}}
    img=mv(:,:,:,i);                        % setting (i) frame for rgb-comparison
    for j=1:2*nbr+1                         % beginning x-loop for comparison
        xx=xy(i-1,2)-(nbr+1-j);             % setting x to be compared
        if xx<1, xx=1; end                  % resetting xx in case it...
        if xx>vw, xx=vw; end                % ...exceeds frame width
        for k=1:2*nbr+1                     % beginning y-loop for comparison
            yy=xy(i-1,3)-(nbr+1-k);         % setting y to be compared
            if yy<1, yy=1; end              % resetting yy in case it...
            if yy>vh, yy=vh; end            % ...exceeds frame height
            cc(j,k,1:3)=img(yy,xx,:);       % acquiring rgb of (xx,yy)
            c1=[cc(j,k,1),cc(j,k,2),cc(j,k,3)];     % setting c1 as rgb of (xx,yy)
            t=sum(abs(c1-c0));              % setting t as rgb-difference of target and (xx,yy)
            if t<min                        %-------------------------------------
                min=t;                      % looking for minimum t
                ncrd=[xx,yy];               % if found, getting its x-y and rgb
                nrgb=c1;                    %
                jk=[j,k];                   %
            else if ((t==min) && (sum(abs([j,k]-[nbr+1,nbr+1]))<sum(abs(jk-[nbr+1,nbr+1]))))
                    ncrd=[xx,yy];           %
                    nrgb=c1;                %
                    jk=[j,k];               % also, preferring new xy closest to pre-xy
                end                         % {{can try some distribution in preference, think properly about low fps vids}}
            end                             %^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        end                                 % ending y-loop
    end                                     % ending x-loop
    if min>=rgbde                           %-------------------------------------
        fprintf('WARNING: High RGB difference of %1.0f detected between frames %2.0f and %3.0f\n',t,i-1,i);
        e1ch=input('Enter a positive integer to change search region for all further frames,\n0 to manually select the point in this frame, -1 to continue: ');
        if e1ch==0                          %
            imshow(img),title(['Reselect the target in frame # ',int2str(i)]);
            xy(i,2:3)=round(ginput(1));     % manual selection of point if RGB difference exceeds rgbde
            xy(i,1)=i/dt;                   %
            xy(i,6:8)=img(xy(i,3),xy(i,2),:);
            i=i+1;                          %
        else if e1ch>0                      %
            nbr=input('Enter new search neighborhood area around the target in pixels: ');    % select new search neighborhood area
            else                            %
                xy(i,[1:3,6:8])=[i,ncrd,nrgb];     % otherwise continue
                i=i+1;                      %
            end                             %
        end                                 %
    else                                    %
        xy(i,[1:3,6:8])=[i/dt,ncrd,nrgb];   %
        i=i+1;                              %
    end                                     %^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    vx=(xy(i-1,2)-xy(i-2,2))/dt;            %
    vy=(xy(i-1,3)-xy(i-2,3))/dt;            %
    xy(i-1,4:5)=[vx,vy];                    %
end                                         % ending frame-loop
vfx=input('Enter scaling factor for x-axis (1 for no change): ');
vfy=input('Enter scaling factor for y-axis (1 for no change): ');
xy(:,2)=xy(:,2)*vfx;                        % scaling x-coordinates
xy(:,3)=(vh-xy(:,3)+1)*vfy;                 % scaling and flipping y-coordinates
xy(:,4)=xy(:,4)*vfx;                        % scaling vx
xy(:,5)=-xy(:,5)*vfy;                       % scaling vy, negating due to flipping of y-axis
clear c0 c1 cc dt e1ch i img j jk k min mvfr nbr ncrd nfr nrgb rgbde t tnfr vdeo vfx vfy vh vsz vw vx vy xx yy
fprintf('Origin is at the left bottom corner of the video.');
fprintf('xy is the result, columns: t-x-y-vx-vy-r-g-b\n');
xy(fr_strt:fr_end,:)