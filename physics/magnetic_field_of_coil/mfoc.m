% Last Updated: 07-Dec-2015
% Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
% Source: https://github.com/udy11, https://gitlab.com/udy11
% Function to compute magnetic field due to
% current carrying coil at any point in space

% ALL YOU NEED TO DO:
% Call tcmfdtac() with:
%   INPUT:
%     uu = permeability constant of the medium
%     cr = coil radius
%     ci = coil current (sign sensitive)
%     ax(3) = direction in which coil axis is pointing (can be unnormalized)
%     xc(3) = co-ordinates of the center of coil
%     xr(3) = co-ordinates at which magnetic field is to be calculated
%   OUTPUT:
%     bm(3) = cartesian components of magnetic field

% NOTE:
% All numbers and calculations in SI Units
% Please read the attached pdf file for the expression of magnetic field
% ax, xc, xr and bm have 3 elements each representing x, y and z
%   components respectively
% Magnetic field blows up at the coil's position, make sure xr is not
%   very near the coil

function bm = tcmfdtac(uu,cr,ci,ax,xc,xr)
    bm=zeros(3,1);
    x2=zeros(3,1);
    ax12=ax(1)*ax(1)+ax(2)*ax(2);
    ax123s=sqrt(ax12+ax(3)*ax(3));
    cth=ax(3)/ax123s;
    sth=sqrt(ax12)/ax123s;
    ph=atan2(ax(2),ax(1));
    cph=cos(ph);
    sph=sin(ph);
    x1=xr+xc;
    x1cs=x1(1)*cph+x1(2)*sph;
    x2(1)=x1cs*cth-x1(3)*sth;
    x2(2)=-x1(1)*sph+x1(2)*cph;
    x2(3)=x1cs*sth+x1(3)*cth;
    x2r=sqrt(x2(1)*x2(1)+x2(2)*x2(2));
    if x2r<2.22044604925032e-16
        tv1=uu*ci*cr*cr*0.5*(1.0/sqrt(cr*cr+x2(3)*x2(3)))^3;
        bm(1)=tv1*cph*sth;
        bm(2)=tv1*sth*sph;
        bm(3)=tv1*cth;
    else
        rt=zeros(3,3);
        x2t=atan2(x2(2),x2(1));
        ck2=4.0*cr*x2r/((x2r+cr)^2+x2(3)^2);
        if ck2==1
            ek=realmax;
        else
            ek=ellipticK(ck2);
        end
        ee=ellipticE(ck2);
        tv1=uu*ci*sqrt(ck2)*0.07957747154594766788/x2r/sqrt(cr*x2r);
        tv2=0.5*ee/(1.0-ck2);
        tv3=tv1*(tv2*(2.0-ck2)-ek)*x2(3);
        bm(1)=tv3*cos(x2t);
        bm(2)=tv3*sin(x2t);
        bm(3)=tv1*(tv2*(ck2*(x2r+cr)-2.0*x2r)+ek*x2r);
        rt(1,1)=cth*cph;
        rt(1,2)=-sph;
        rt(1,3)=sth*cph;
        rt(2,1)=cth*sph;
        rt(2,2)=cph;
        rt(2,3)=sth*sph;
        rt(3,1)=-sth;
       % rt(3,2)=0.0;
        rt(3,3)=cth;
        bm=rt*bm;
    end
end
